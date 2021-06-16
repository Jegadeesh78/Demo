#import libraries
import numpy as np
from flask import Flask, render_template,request
import pickle


app = Flask(__name__)


model = pickle.load(open('D:\\Jagadeesh_folder\\Machine learning\\Eng_josaaNew.pkl', 'rb'))

#default page of our web-app
@app.route('/')
def home():
    State = ['Haryana','Pondicherry','Telangana','Chandigarh','West Bengal','Jammu and Kashmir','Jharkhand','Chhattisgarh','Uttar Pradesh','Madhya Pradesh','Assam','Maharashtra','Gujarat','Uttarakhand','Tamil Nadu','Odisha','Mizoram','Manipur','Arunachal Pradesh','Sikkim','Puducherry','Bihar','Nagaland','Meghalaya','Karnataka','Himachal Pradesh','Goa','Delhi','Kerala','Tripura','Rajasthan','Punjab']
          
    return render_template("Newjosaa.html",c=State)

@app.route('/hello', methods=['GET', 'POST'])
def hello(): 
    if request.method == "POST" :
        if request.json["inst_no"]:
            data = request.json["inst_no"]
            print(data)
            d=[]
            #e=[]
            #my_dict3={'Chennai':1,'South West Delhi':2,'Mumbai Suburban':3,'Paschim Bardhaman':4,'Kanpur':5,'Haridwar':6,'Sangareddy':7,'Indore':8,'Khordha':9,'Mandi':10,'Patna':11,'Gandhinagar':12,'Kozhikode':13,'Rupnagar':14,'Jodhpur':15,'Hamirpur':16,'East Khasi Hills':17,'West Tripura':18,'Raipur':19,'South Goa':20,'Kamrup Metropolitan':21,'Dimapur':22,'South Sikkim':23,'Papum Pare':24,'Karaikal':25}
            city = {
                'Haryana': ['Sonipat'],
                'Pondicherry': ['Puducherry','Thiruvettakudy'],                                                 
                'Telangana': ['Hyderabad','Hanmakonda'],
                'Chandigarh': ['Chandigarh'],
                'West Bengal': ['Shibpur'],                                                 
                'Jammu and Kashmir': ['Katra','Srinagar'],
                'Jharkhand': ['Ranchi'],
                'Chhattisgarh': ['Bilaspur','Raipur'],                                                 
                'Uttar Pradesh': ['Bhadohi','Allahabad','Varanasi','Kanpur'],
                'Madhya Pradesh': ['Jabalpur','Indore'],
                'Assam': ['Guwahati','Silchar'],                                                 
                'Maharashtra': ['Nagpur','Mumbai'],
                'Gujarat': ['Surat','Gandhinagar'],
                'Uttarakhand': ['Srinagar (Garhwal)','Roorkee'],                                                 
                'Tamil Nadu': ['Tiruchirappalli','Chennai','Thanjavur'],
                'Odisha': ['Rourkela','Bhubaneswar'],
                'Mizoram': ['Aizawl'],                                                 
                'Manipur': ['Imphal'],
                'Haryana': ['Kurukshetra'],
                'Jharkhand': ['Jamshedpur','Dhanbad'],                                                 
                'Arunachal Pradesh': ['Yupia','Itanagar'],
                'Sikkim': ['Nanchi'],
                'Bihar': ['Patna'],                                                 
                'Nagaland': ['Dimapur'],
                'Meghalaya': ['Shillong'],
                'Karnataka': ['Surathkal'],
                'Himachal Pradesh': ['Hamirpur','Mandi'],
                'Goa': ['Ponda'],
                'West Bengal': ['Durgapur','Kharagpur'],
                'Delhi': ['New Delhi','Delhi'],
                'Kerala': ['Kozhikode'],
                'Tripura': ['Agratala'],
                'Rajasthan': ['Jaipur','Jodhpur']
                }
            search = data
            for key, value in city.items(): 
                if key == search:
                    for x in value:
                        d.append(x)
            print(d)            
            
            final=''
            a_list = d
            two_split = np.array_split(a_list, len(a_list))
            for array in two_split:
                array = str(array)[1:-1] 
                array=array.replace("'", "") 
                attach ='<option value="{no}">{college}</option>'.format(no=array,college=array)
                final =final+attach
                print(final)
            final='<option value="" disabled selected>SELECT</option>'+ final   
            return final
    #return render_template("flaskdemo12.html",final=final)

#To use the predict button in our web-app
@app.route('/predict',methods=['POST'])
def predict():
    #For rendering results on HTML GUI
    if request.method == "POST":
        dictOfWords = {'National Institute of Food Technology, Enterprenurship & Management':1,'Pondicherry Engineering College':2,'Jawaharlal Nehru Technological University':3,'Punjab Engineering College (Deemed To Be University)':4,'University College of Engineering':5,'Indian Institute of Engineering Science and Technology':6,'Shri Mata Vaishno Devi University':7,'National Institute of Foundry and Forge Technology':8,'Guru Ghasidas Vishwavidyalaya':9,'Indian Institute of Carpet Technology Bhadohi':10,'Pandit Dwarka Prasad Mishra Indian Institute of Information Technology, Design and Manufacturing (IIITDM) Jabalpur':11,'Indian Institute of Information Technology Allahabad':12,'Indian Institute of Information Technology Guwahati':13,'Visvesvaraya National Institute of Technology':14,'Sardar Vallabhbhai National Institute of Technology':15,'National Institute of Technology Warangal':16,'National Institute of Technology Uttarakhand':17,'National Institute of Technology Tiruchirappalli':18,'National Institute of Technology Srinagar':19,'National Institute of Technology Silchar':20,'National Institute of Technology Rourkela':21,'National Institute of Technology Mizoram':22,'National Institute of Technology Manipur':23,'National Institute of Technology Kurukshetra':24,'National Institute of Technology Jamshedpur':25,'National Institute of Technology Arunachal Pradesh':26,'National Institute of Technology Sikkim':27,'National Institute of Technology Raipur':28,'National Institute of Technology Puducherry':29,'National Institute of Technology Patna':30,'National Institute of Technology Nagaland':31,'National Institute of Technology Meghalaya':32,'National Institute of Technology Karnataka':33,'National Institute of Technology Hamirpur':34,'National Institute of Technology Goa':35,'National Institute of Technology Durgapur':36,'National Institute of Technology Delhi':37,'National Institute of Technology Calicut':38,'National Institute of Technology Agartala':39,'Malaviya National Institute of Technology':40,'Indian Institute of Technology Guwahati':41,'Indian Institute of Technology (Banaras Hindu University) Varanasi':42,'Indian Institute of Technology Ropar':43,'Indian Institute of Technology (Indian School of Mines) Dhanbad':44,'Indian Institute of Technology Roorkee':45,'Indian Institute of Technology Patna':46,'Indian Institute of Technology Gandhinagar':47,'Indian Institute of Technology Madras':48,'Indian Institute of Technology Kanpur':49,'Indian Institute of Technology Jodhpur':50,'Indian Institute of Technology Hyderabad':51,'Indian Institute of Technology Kharagpur':52,'Indian Institute of Technology Indore':53,'Indian Institute of Technology Delhi':54,'Indian Institute of Technology Mandi':55,'Indian Institute of Technology Bombay':56,'Indian Institute of Technology Bhubaneswar':57,'North Eastern Regional Institute of Science & Technology':58,'Indian Institute of Food Processing Technology (IIFPT)':59}
        
        rou = request.form.get("Round")
        rou1=float(rou)
        cat = request.form.get("Category")
        cat1=float(cat)
        Course = request.form.get("Academic Program Name")
        Course1=float(Course)
        Quot = request.form.get("Quota")
        Quot1=float(Quot)
        Seat= request.form.get("Seat Type")
        Seat1=float(Seat)
        Gend = request.form.get("Gender")
        Gend1=float(Gend)
        JosaaopRank = request.form.get("Josaa Opening Rank")
        JosaaopRank1=float(JosaaopRank)
        JosaaCloRank = request.form.get("Josaa Closing Rank")
        JosaaCloRank1=float(JosaaCloRank)
        NIRF = request.form.get("NIRF rank")
        NIRF1=float(NIRF)
        NAAC = request.form.get("NAAC Grade")
        NAAC1=float(NAAC)
        my_dict2={'Haryana': 1, 'Pondicherry': 2, 'Telangana': 3, 'Chandigarh': 4, 'West Bengal': 5, 'Jammu and Kashmir': 6, 'Jharkhand': 7, 'Chhattisgarh': 8, 'Uttar Pradesh': 9, 'Madhya Pradesh': 10, 'Assam': 11, 'Maharashtra': 12, 'Gujarat': 13, 'Uttarakhand': 14, 'Tamil Nadu': 15, 'Odisha': 16, 'Mizoram': 17, 'Manipur': 18, 'Arunachal Pradesh': 19, 'Sikkim': 20, 'Puducherry': 21, 'Bihar': 22, 'Nagaland': 23, 'Meghalaya': 24, 'Karnataka': 25, 'Himachal Pradesh': 26, 'Goa': 27, 'Delhi': 28, 'Kerala': 29, 'Tripura': 30, 'Rajasthan': 31, 'Punjab': 32}
        State = request.form.get("State")
        listOfKeys1 = [value  for (key, value) in my_dict2.items() if key ==State]
        listOfKeys1 = str(listOfKeys1)[1:-1]
        State1=float(listOfKeys1)
        my_dict3={'Sonipat': 1, 'Puducherry': 2, 'Hyderabad': 3, 'Chandigarh': 4, 'Shibpur': 5, 'Katra': 6, 'Ranchi': 7, 'Bilaspur': 8, 'Bhadohi': 9, 'Jabalpur': 10, 'Allahabad': 11, 'Guwahati': 12, 'Nagpur': 13, 'Surat': 14, 'Hanmakonda': 15, 'Srinagar (Garhwal)': 16, 'Tiruchirappalli': 17, 'Srinagar': 18, 'Silchar': 19, 'Rourkela': 20, 'Aizawl': 21, 'Imphal': 22, 'Kurukshetra': 23, 'Jamshedpur': 24, 'Yupia': 25, 'Nanchi': 26, 'Raipur': 27, 'Thiruvettakudy': 28, 'Patna': 29, 'Dimapur': 30, 'Shillong': 31, 'Surathkal': 32, 'Hamirpur': 33, 'Ponda': 34, 'Durgapur': 35, 'New Delhi': 36, 'Kozhikode': 37, 'Agratala': 38, 'Jaipur': 39, 'Varanasi': 40, 'Rupnagar': 41, 'Dhanbad': 42, 'Roorkee': 43, 'Gandhinagar': 44, 'Chennai': 45, 'Kanpur': 46, 'Jodhpur': 47, 'Kharagpur': 48, 'Indore': 49, 'Delhi': 50, 'Mandi': 51, 'Mumbai': 52, 'Bhubaneswar': 53, 'Itanagar': 54, 'Thanjavur': 55}
        City = request.form.get("City")
        print(City)
        listOfKeys2 = [value  for (key, value) in my_dict3.items() if key ==City]
        print(listOfKeys2)
        listOfKeys2 = str(listOfKeys2)[1:-1]
        City1=float(listOfKeys2)
        BHostels = request.form.get("Boys Hostels")
        BHostels1=float(BHostels)
        GHostels = request.form.get("Girls Hostels")
        GHostels1=float(GHostels)
        Intake = request.form.get("UG Approved Intake")
        Intake1=float(Intake)
        Studentsadmitted = request.form.get("Students admitted in UG")
        Studentsadmitted1=float(Studentsadmitted)
        StudentsPlaced = request.form.get("Students Placed in UG")
        StudentsPlaced1=float(StudentsPlaced)
        MedianSalaryUG = request.form.get("Median Salary UG")
        MedianSalaryUG1=float(MedianSalaryUG)
        
        int_features = [rou1,cat1,Course1,Quot1,Seat1,Gend1,JosaaopRank1,JosaaCloRank1,NIRF1,NAAC1,State1,City1,BHostels1,GHostels1,Intake1,Studentsadmitted1,StudentsPlaced1,MedianSalaryUG1]
        final_features = [np.array(int_features)]
        prediction = model.predict(final_features)
        print(prediction)
        output =round( prediction[0],2 )
    #print(output)
        output1 = round(output)
        print(output1)
    #split_num = str(output).split('.')
    #int_part = int(split_num[0])
   # print(int_part)
        listOfKeys = [key  for (key, value) in dictOfWords.items() if value ==output1]
        listOfKeys = str(listOfKeys)[1:-1]
        listOfKeys = listOfKeys.strip("''")
        print(listOfKeys)
    return render_template('Newjosaa.html', prediction_text='predicted colleges is : {}'.format(listOfKeys))


if __name__ == "__main__":
    app.run(debug=True)
    