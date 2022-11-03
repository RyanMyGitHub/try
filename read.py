import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

#doc_ref = db.document("靜宜資管/tcyang")
#doc = doc_ref.get()
#result = doc.to_dict()
#print("文件內容為：{}".format(result))
#print(result["name"]+"的mail是"+result["mail"])

cond = input("請輸入課程關鍵字：")

collection_ref = db.collection("111")
docs = collection_ref.get()
for doc in docs:
    dict = doc.to_dict()
    if cond in dict["Course"]:
        print(format(dict["Leacture"])+"老師開的"+format(dict["Course"])+"課程,每週"+format(dict["Time"])+"於"+format(dict["Room"])+"上課")

