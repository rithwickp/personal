import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
username = "ritpal.1207@gmail.com" 
password = "u,qALn8Qm4gfh!!"
driver = webdriver.Chrome()
profiles = []
driver.get("https://www.linkedin.com/login")
driver.find_element(By.ID, "username").send_keys(username)
driver.find_element(By.ID, "password").send_keys(password)
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
with open('C:\\Users\\rpal2\\Downloads\\result.csv') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        link = row[0]
        driver.get(link)

        #driver.get("https://www.linkedin.com/in/kathleenthogan")
        #assert "Python" in driver.title
        #test_elem = driver.find_element(By.ID, "nojs")
        #test_elemt = test_elem.text
        
        #name = driver.find_element_by_tag_name("h1").text
        name = driver.find_element(By.TAG_NAME, "h1").get_attribute("innerText")
            
        #job_title = driver.find_element(By.TAG_NAME, "h2").get_attribute("innerText")     
        job_title = driver.find_element(By.XPATH, value="./*")
        
        about = driver.find_element(By.CLASS_NAME, "text-body-medium").get_attribute("innerText") 
        #about = driver.find_element(By.TAG_NAME, "p").text
        
        experiences = driver.find_elements(By.CLASS_NAME, "experience__list")
        experience_list = []
        for experience in experiences:
            title = experience.find_element(By.TAG_NAME, "h3").get_attribute("innerText")
            company = experience.find_element(By.CLASS_NAME, "experience-group-header__company").get_attribute("innerText")
            date_range = experience.find_element(By.CLASS_NAME, "experience-group-header__duration").get_attribute("innerText")
            experience_list.append((title, company, date_range))
            print(title)
        experience_list = [exp.text for exp in experiences]
        print(experience_list)

        time.sleep(0.5)
        
        education = driver.find_elements(By.CLASS_NAME, "education__list")
        education_list = []
        for edu in education:
            school = edu.find_element(By.CLASS_NAME,"profile-section-card__title-link").get_attribute("innerText")
            degree = edu.find_element(By.CLASS_NAME,"profile-section-card__subtitle").get_attribute("innerText")
            education_list.append((school, degree))
        education_list = [edu.text for edu in education]    
        time.sleep(0.5)
        print(education_list)
        #skills_section = driver.find_element(By.CLASS_NAME, "core-section-container my-3 core-section-container--with-border border-b-1 border-solid border-color-border-faint m-0 py-3 pp-section skills") 
        #skills = skills_section.find_elements(By.CLASS_NAME, "show-more-less__list show-more-less__list--no-hidden-elems")
        #skills_list = []
        #for skill in skills:
            #skill_name = skill.find_element(By.CLASS_NAME, "skills__item skills__item--link").get_attribute("innerText")
            #skills_list.append(skill_name)
            
        #locate link to expand skills
        #show_more_skills_button = driver.find_element(By.CLASS_NAME,"show-more-less__list show-more-less__list--no-hidden-elems")
        #expand
        #show_more_skills_button.click()
        #skills = driver.find_elements(By.XPATH,"//*[starts-with(@class,'pv-skill-category-entity__name-text')]")
        #create skills set
        #skill_set = []
        #for skill in skills:
           # skill_set.append(skill.text)
        time.sleep(0.5)
        #connections = driver.find_element(By.CLASS_NAME,"top-card__subline-item top-card__subline-item--bullet").get_attribute("innerText")
        profile = {
            "name": name,
            "job_title": job_title,
            "about": about,
            "experiences": experience_list,
            "education": education_list
        }
        print(profile)
        time.sleep(3)
        profiles.append(profile)
        time.sleep(10)
time.sleep(2)        
with open("profiles_data.csv", 'w', newline='') as output_file:
    writer = csv.writer(output_file)
    writer.writerow(['Name', 'Job Title', 'About', 'Experiences', 'Education'])
    for profile in profiles:
        writer.writerow([profile['name'], profile['job_title'], profile['about'], ';'.join(profile['experiences']), ';'.join(profile['education'])])
driver.close() 