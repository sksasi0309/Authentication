x=document.getElementsByTagName("input");
        y=document.getElementsByTagName("p");
        function onMouseover(i)
        {
            if(x[i].value=="")
            {
                y[i].innerHTML='pleace fill this field' 
            }

        }
        function onMouseout(i)
        {
            y[i].innerHTML="";
        }
        function check()
        {
            fname=document.getElementById("fname").value
            lname=document.getElementById("lname").value
            mobile=document.getElementById("mobile").value
            email=document.getElementById("email").value;
            password=document.getElementById("password").value;
            cpassword=document.getElementById("cpassword").value
            if(fname=="")
            {
                alert("pleace fill the FIRST NAME");
                return false
            }
            else if(lname=="")
            {
                alert("pleace fill the LAST NAME");
                return false
            }
            else if(mobile=="")
            {
                alert("pleace fill the MOBILE");
                return false
            }
            else if(email=="")
            {
                alert("pleace fill the EMAIL ID");
                return false
            }
            else if(password=="")
            {
                alert("pleace fill the PASSWORD");
                return false
            }
            else if(cpassword=="")
            {
                alert("pleace fill the CONFIRM PASSORD");
                return false
            }
            
        }