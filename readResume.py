from pypdf import PdfReader
import json


class Reader:

    def __init__(self):
        self.keywords = []

    def readResume(self): 
        reader = PdfReader('resume2.pdf')
        pageObj = reader.pages[0]
        text = pageObj.extract_text()
       
        startPoint = "SKILLS"
        endPoint = "SUMMARY" 

        startIndex = text.find(startPoint)
        
        endIndex = text.find(endPoint)

        if startIndex != -1 and endIndex != -1 and endIndex > startIndex:
            skillsSection = text[startIndex + len(startPoint):endIndex].strip()
            raw_skills = skillsSection.replace('\n', ',')
            split_skills = [skill.strip() for skill in raw_skills.split(',') if skill.strip()]
            for skill in split_skills:
                if "robert" in skill.lower() or "ballard" in skill.lower():
                    break
                self.keywords.append(skill)
        else:
            print("[INFO] Could not find specified markers or invalid order.")
 


    def convertToJson(self, filename="userResume.json"):
        with open(filename, "w") as f:
            json.dump(self.keywords, f, indent=4)
        print(f"[INFO] Saved {len(self.keywords)} keywords to '{filename}'")
