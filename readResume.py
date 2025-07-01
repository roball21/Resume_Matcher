from pypdf import PdfReader
import json


class Reader:

    def __init__(self):
        self.keywords = []
        self.resume_text = ""

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
 

    def keywords_to_text(self):
        if not self.keywords:
            return ""
        skill_phrases = {
            "C++": "experience in C++",
            "Python": "experience in Python",
            "MySQL": "skills in MySQL database management",
            "Windows": "familiarity with Windows systems",
            "Linux": "familiarity with Linux environments",
            "Data Structures and Algorithms": "strong knowledge of data structures and algorithms",
            "Critical Thinking": "strong critical thinking skills",
            "Time Management": "effective time management abilities"
        }
        sentences = [
            skill_phrases.get(skill, f"proficiency in {skill}")
            for skill in self.keywords
        ]
        if not sentences:
            self.resume_text = ""
            return ""
        
        summary = "I have " + ", ".join(sentences[:-1])
        if len(sentences) > 1:
            summary += ", and " + sentences[-1] + "."
        else:
            summary += sentences[0] + "."

        self.resume_text = summary    
        return summary



    def convertToJson(self, filename="userResume.json"):
        if not self.resume_text:
          print("[WARN] Resume text is empty. Run keywords_to_text() first.")
          return  
        with open(filename, "w") as f:
            json.dump({"resume": self.resume_text}, f, indent=2)
        print(f"[INFO] Saved resume to '{filename}'")
