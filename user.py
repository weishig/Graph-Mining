class user:
   def __init__(self,id,age,gender,occupation,zip_code):
      self.age = age
      self.id = id
      self.gender=gender
      self.occupation=occupation
      self.zip=zip_code

 
   def printUserInfor(self):
     print("User id ="+str(self.id)+", age="+str(self.age)+", gender="+str(self.gender)+", occupation="+str(self.occupation)+", zip code="+str(self.zip))
 
