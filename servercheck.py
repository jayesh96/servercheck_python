import subprocess,json
import smtplib


url = "Enter your Url Here"
login_email = "Enter your Email Here" #Enter your Gmail Email
login_password = "Enter your password Here" #Enter your Gmail Password

#Add Email Reciepents here
li = ['abc@g.com','test123@g.com']
 
def main():
    
    try:
        proc = subprocess.Popen(["curl" ,"-s",url], stdout=subprocess.PIPE)
        (out, err) = proc.communicate()
        d = json.loads(out)
        if type(d['status']) == type(True):
            print ("Working Fine");
        
        else:
            msg =  "<---------- Server Is NOT Working Fine --------->"
            try:
                print(len(li))
                for i in range(len(li)):
                    s = smtplib.SMTP('smtp.gmail.com', 587)
                    s.starttls()
                    s.login(login_email, login_password)
                    message = msg
                    s.sendmail(login_email, li[i], message)
                    s.quit()
            except:
                print ("Error in smtp");

    except:
        msg =  "Server Is NOT Working Fine"
        for i in range(len(li)):
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login(login_email, login_password)
                message = msg
                s.sendmail(login_email, li[i], message)
                s.quit()





if __name__ == '__main__':
    print ("Plese Wait While we test the server");
    main()



# IMPORTANT NOTES
# MAKE SURE GMAIL CAN SEND MAIL USING SMTP PORT
# if you want to automotically check you can add a cron job by using command crontab -e for ubuntu/mac users
# * * * * * python /home/ubuntu/server_check.py >> /home/ubuntu/crons.txt
# This will automatically build log after every one interval


