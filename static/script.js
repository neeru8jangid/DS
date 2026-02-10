// script.js — POST to /predict, display results. Save in same folder.

(() => {
  document.addEventListener('DOMContentLoaded', () => {
    const btnPredict = document.getElementById('btnPredict');
    const btnReset = document.getElementById('btnReset');
    const mockCheckbox = document.getElementById('mockCheckbox');
    const resultsPanel = document.getElementById('resultsPanel');
    const resultCrop = document.getElementById('resultCrop');
    const resultNotes = document.getElementById('resultNotes');
    const apiError = document.getElementById('apiError');

    function getInputValues(){
      return {
        N: parseFloat(document.getElementById('N').value),
        P: parseFloat(document.getElementById('P').value),
        K: parseFloat(document.getElementById('K').value),
        temperature: parseFloat(document.getElementById('temperature').value),
        humidity: parseFloat(document.getElementById('humidity').value),
        ph: parseFloat(document.getElementById('ph').value),
        rainfall: parseFloat(document.getElementById('rainfall').value)
      };
    }

    function validate(payload){
      for(const k of Object.keys(payload)){
        if (Number.isNaN(payload[k])) return k;
      }
      return null;
    }

    async function doPredict(){
      apiError.hidden = true;
      resultsPanel.hidden = true;

      const payload = getInputValues();
      const invalid = validate(payload);
      if(invalid){
        apiError.textContent = `Please enter a valid number for ${invalid}.`;
        apiError.hidden = false;
        return;
      }

      // loading state
      btnPredict.disabled = true;
      btnPredict.textContent = 'Working…';

      // MOCK mode for UI testing (no backend needed)
      if (mockCheckbox && mockCheckbox.checked){
        await new Promise(r=>setTimeout(r,700));
        resultCrop.textContent = "Wheat (mock)";
        resultNotes.textContent = "Mock notes: soil N moderate; monitor irrigation. Use MOCK to test UI.";
        resultsPanel.hidden = false;
        btnPredict.disabled = false;
        btnPredict.textContent = 'Generate Recommendation';
        return;
      }

      try {
        const resp = await fetch('/predict', {
          method: 'POST',
          headers: {'Content-Type':'application/json'},
          body: JSON.stringify(payload)
        });

        if(!resp.ok){
          const txt = await resp.text();
          throw new Error(txt || `${resp.status} ${resp.statusText}`);
        }

        const data = await resp.json();

        // repo's /predict returns { recommended_crop: "...", maybe notes... }
        resultCrop.textContent = data.recommended_crop || data.crop || 'No crop returned';
        resultNotes.textContent = data.notes || data.general_note || 'No extra notes returned.';
        resultsPanel.hidden = false;
      } catch(err){
        apiError.textContent = 'Prediction failed — ' + (err.message || 'unknown error');
        apiError.hidden = false;
      } finally {
        btnPredict.disabled = false;
        btnPredict.textContent = 'Generate Recommendation';
      }
    }

    btnPredict.addEventListener('click', doPredict);
    btnReset.addEventListener('click', ()=>{
      document.getElementById('predictForm').reset();
      resultsPanel.hidden = true;
      apiError.hidden = true;
    });

    // minimal chat UI behaviour (placeholder)
    const chatSend = document.getElementById('chatSend');
    if(chatSend){
      chatSend.addEventListener('click', ()=>{
        const q = document.getElementById('chatInput').value.trim();
        if(!q) return;
        const box = document.getElementById('chatBox');
        const el = document.createElement('div');
        el.textContent = `You: ${q}`;
        el.style.marginBottom = '6px';
        box.appendChild(el);
        document.getElementById('chatInput').value = '';
        // Placeholder: real chatbot would call a /chat endpoint or Gemini
        const bot = document.createElement('div');
        bot.textContent = "Assistant: (chat integration not enabled) — enable Gemini/OpenAI integration in server to use.";
        bot.style.opacity = '0.9';
        bot.style.marginBottom = '8px';
        box.appendChild(bot);
        box.scrollTop = box.scrollHeight;
      });
    }
  });
})();
