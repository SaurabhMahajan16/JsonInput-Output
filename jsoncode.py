
import json
#json class as we are using loads, dump function

print("paste your json here")

#taking input Json string from the user paste your launched bookmark in input
#make sure everything has doublequotes otherwise it will throw an error there is no expection handling
inputJsonString=input()
#inputJson="\"\"\""+inputJsonString+"\"\"\""
#print(inputJson)

#Output string is the string from which you will get replica of bookmark
outputString="""{
"username": "",
"user_id": "aaa",
"email": "",
"registration_id": "ddd3f1df-9942-4457-b8da-2d206e5ae901",
"lesson_id": "MOT",
"lesson_name": "MDV_Safe Highway Driving_01",
"lesson_description": "",
"lesson_result": "",
"country_code": "US",
"language_code": "en",
"vehicle_type": "MDV",
"version_code": "null",
"redirect_url": "https://fd.fleetdefense.com/mod/adxapilaunch/complete.php?id=36118",
"lesson_scoring_type": "DDT",
"pass_mark": "90",
"lesson_source": "LMS",
"lfv2": "",
"name": "Gerold Chavis",
"lesson_uri": "https://fleetdefense.com/MOT_01/MDV_MOT",
"course_id": "4746",
"license_id": "7120",
"course_name": "MDV_Safe Highway Driving_01",
"length": null,
"clear": null,
"getItem": null,
"key": null,
"removeItem": null,
"setItem": null,
"task_id": 6418,
"task_name": "Title Screen0",
"content": [{
"content_type": "other",
"content_id": 0,
"category": "task",
"properties": {}
}]
}"""


#this function doesnt have much use now but may be if something gets depreciated in that case it can be used
def addquotes(value):
   return "\""+value+"\""
#input2=json.dumps(inputJsonString)


#print(inputJsonString)just for debugging
#this is inbuilt function of Json class which converts string to Json Object
json_object=json.loads(inputJsonString)
#json_formatted_str = json.dumps(json_object, indent=2)
#print(json_formatted_str)


getEmail=json_object["statement"]["actor"]["mbox"]
email_quotes=addquotes(getEmail)

getUserName=json_object["statement"]["actor"]["name"]
UserName_quotes=addquotes(getUserName)
#print(UserName_quotes)


getRegistration=json_object["statement"]["context"]["registration"]
registration_quotes=addquotes(getRegistration)

#getCourseName=["statement"]["context"]["parent"]["defintion"]["name"]["en-US"]
#courseName_quotes=addquotes(getCourseName)

getLessonCode=json_object["statement"]["context"]["extensions"]["http://fleetdefense.com/extensions/lessoncode"]
lessonId_quotes=addquotes(getLessonCode)

getLanguage=json_object["statement"]["context"]["language"]
language_quotes=addquotes(getLanguage)

getCountry=json_object["statement"]["context"]["extensions"]["http://fleetdefense.com/extensions/countrycode"]
countryCode_quotes=addquotes(getCountry)

getvehicleType=json_object["statement"]["context"]["extensions"]["http://fleetdefense.com/extensions/vehicletype"]
vehicle_quotes=addquotes(getvehicleType)

getVersion=json_object["statement"]["context"]["extensions"]["http://fleetdefense.com/extensions/versioncode"]
#version_quotes=addquotes(getVersion)

getlessonScoringType=json_object["statement"]["context"]["extensions"]["http://fleetdefense.com/extensions/lessonscoringtype"]
lessonScoringType_quotes=addquotes(getlessonScoringType)

getredirecturl=json_object["statement"]["context"]["extensions"]["http://fleetdefense.com/extensions/redirecturl"]
redirectUrl_quotes=addquotes(getredirecturl)

getMasteryScore=json_object["statement"]["context"]["extensions"]["https://w3id.org/xapi/cmi5/context/extensions/masteryscore"]
#masteryScore_quotes=addquotes(getMasteryScore)


getlessonsource=json_object["statement"]["context"]["extensions"]["http://fleetdefense.com/extensions/lessonsource"]
lessonSource_quotes=addquotes(getlessonsource)

getLicenseId=json_object["statement"]["context"]["extensions"]["http://fleetdefense.com/extensions/licenseid"]
licenseId_quotes=addquotes(getLicenseId)

getUserId=json_object["statement"]["context"]["extensions"]["http://fleetdefense.com/extensions/username"]
userId_quotes=addquotes(getUserId)

getLessonName=json_object["statement"]["object"]["definition"]["name"][getLanguage]
lessonName_quotes=addquotes(getLessonName)
print(getLessonName)


getLessonUri=json_object["statement"]["object"]["id"]
lessonUri_quotes=addquotes(getLessonUri)


getCourseidString=json_object["relatedActivities"][1]
getCourseId=getCourseidString[-4:]
courseId_quotes=addquotes(getCourseId)



#json_output_object=json.loads(inputJson)
#json_formatted_str_output = json.dumps(json_output_object, indent=2)

#assigning values to your output json bookmark
json_object=json.loads(outputString)
json_object["user_id"]=getUserId
json_object["email"]=getEmail
json_object["registration_id"]=getRegistration
json_object["lesson_id"]=getLessonCode
json_object["lesson_name"]=getLessonName
json_object["country_code"]=getCountry
json_object["language_code"]=getLanguage
json_object["vehicle_type"]=getvehicleType
json_object["version_code"]=getVersion
json_object["redirect_url"]=getredirecturl
json_object["lesson_scoring_type"]=getlessonScoringType
json_object["pass_mark"]=getMasteryScore
json_object["lesson_source"]=getlessonsource
json_object["name"]=getUserName
json_object["lesson_uri"]=getLessonUri
json_object["course_id"]=getCourseId
json_object["license_id"]=getLicenseId

#indent is used for formatting your json file
json_formatted_str = json.dumps(json_object, indent=2)
print("\n Your bookmark is \n\n[" + json_formatted_str + "]")

#copy your output bookmark from output and change value of course name manually
