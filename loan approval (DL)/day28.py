# import pandas as pd
# df= pd.read_csv('loan_approval_dataset.csv')
# df.head()
# df.columns=['loan_id', 'no_of_dependents', 'education', 'self_employed',
#        'income_annum', 'loan_amount', 'loan_term', 'cibil_score',
#        'residential_assets_value', 'commercial_assets_value',
#        'luxury_assets_value', 'bank_asset_value', 'loan_status']
# df['loan_status'].value_counts()
# graduate_ppl = df[df['education'] == "Graduate"]
# not_graduate_ppl = df[df['education']=="NotGraduate"]
# column_name = ['self_employed','loan_status','education']
# for column in column_name:
#     df[column] = df[column].str.replace(' ', '')

# print(df)
# self = df[df['self_employed']== 'Yes']
# self['loan_status'].value_counts()
# nself = df[df['self_employed']== 'No']
# nself['loan_status'].value_counts()
# df2  = graduate_ppl[(graduate_ppl['self_employed']=='Yes')&(graduate_ppl['cibil_score'] >=700)&(graduate_ppl['income_annum'] >= 5065720.930232558
# )]
# graduate_ppl.shape
# df2['loan_status'].value_counts()
# import seaborn as sns
# import matplotlib.pyplot as plt
# sns.relplot(x='income_annum',y="loan_amount",data=df) 
# plt.show()
# df3 = pd.get_dummies(df,drop_first='if_binary').astype(int)
# df3.columns

# sns.relplot(x='income_annum',y="residential_assets_value",data=df,hue='self_employed',) 
# plt.show()
# df3.drop('loan_id',axis=1,inplace=True)

# x = df3.drop('loan_status_Rejected',axis=1)
# y = df3[['loan_status_Rejected']]   

# ### ANN standard scaled
# from sklearn.preprocessing import StandardScaler
# scaler = StandardScaler()

# X = scaler.fit_transform(x)

# from sklearn.model_selection import train_test_split
# x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=0.2)
# import tensorflow as tf
# from tensorflow.keras.layers import Dense #hidden layer
# from tensorflow.keras.models import Sequential
# x_train.shape

# ann_model = Sequential()
# ann_model.add(Dense(units=68,activation='relu',input_dim=11))
# # hidden layer
# ann_model.add(Dense(units=32,activation='relu'))
# ann_model.add(Dense(units=12,activation='relu'))
# # ouput layer
# ann_model.add(Dense(units=1,activation='sigmoid'))

# ann_model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
# ann_model.summary()
# #training model
# history = ann_model.fit(x_train,y_train,epochs=5,validation_data=(x_test,y_test))
# ann_model.evaluate(x_train,y_train)
# ann_model.evaluate(x_test,y_test)
# import pandas as pd
# history=pd.DataFrame(history.history)
# history
# history.plot()
# prediction=ann_model.predict(x_test)
# prediction[0][0]
# predictions = (prediction <0.5).astype(int).ravel()
# predictions
# from sklearn.metrics import confusion_matrix
# from sklearn.metrics import classification_report
# matrix = confusion_matrix(y_test,predictions)
# import seaborn as sns
# sns.heatmap(matrix)
# matrix
# cr = classification_report(y_test,predictions)
# print(cr)

# #model save
# ann_model.save("ann_model.h5")
# import joblib
# joblib.dump(scaler,'scaler.lb')

# from tensorflow.keras.models import load_model
# model = load_model('ann_model.h5')
# model.summary()


