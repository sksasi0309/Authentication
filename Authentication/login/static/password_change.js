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
            password=document.getElementById("password").value;
            cpassword=document.getElementById("cpassword").value;
            if(password=="")
            {
                alert("pleace fill the password");
                return false
            }
            else if(cpassword=="")
            {
                alert("pleace fill the confirm password");
                return false
            }
        }