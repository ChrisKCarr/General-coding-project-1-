
# coding: utf-8

# In[ ]:


def discount(age, major, is_in_military, gpa):
    discount = True
    
    if major == "Computer Science" and gpa >=3.2:
        discount = True

    elif is_in_military == True or age >= 70:
        discount = True
    else:
        discount = False
            
    return discount


def calculate_cost(plan,num_minutes,num_text):
    ans = None
    
    basic = 15 + (num_minutes > 100 and num_minutes-100)*1.5 +(num_text > 1000 and num_text-1000)*.75
    standard = 20 + (num_minutes > 175 and num_minutes-175)*1.25 +(num_text > 1500 and num_text-1500)*.5
    premium = 25 + (num_minutes > 250 and num_minutes-250)*1 +(num_text > 2000 and num_text-2000)*.25
    if plan =='basic':
        ans = basic
    elif plan =='standard':
        ans = standard
    elif plan == 'premium':
        ans = premium
            
    return ans
    

def cost_efficient_plan(age,major,is_in_military,gpa,num_minutes,num_text):
    
        
    basic = 10 + (num_minutes > 100 and num_minutes-100)*1.5 +(num_text > 1000 and num_text-1000)*.75
    standard = 15 + (num_minutes > 175 and num_minutes-175)*1.25 +(num_text > 1500 and num_text-1500)*.5
    premium = 20 + (num_minutes > 250 and num_minutes-250)*1 +(num_text > 2000 and num_text-2000)*.25
    
    if major == "Computer Science" and gpa >= 3.2 and basic*.8 < standard and basic*.8 < premium : 
        ans = ('basic')
        
    elif is_in_military == True and basic*.8 < standard and basic*.8 < premium:
        ans = ('basic')
        
    elif  age >= 70 and basic*.8 < standard and basic*.8 < premium:
        ans = ('basic')
        
    elif basic < standard and basic < premium:
        ans = ('basic')
        
    elif standard < basic and standard < premium:
        ans = ('standard')
        
    elif premium < basic and premium < standard:
        ans = ('premium')
            
    return ans


cost_efficient_plan(20, "Physics", True, 3.5, 180, 1700)

