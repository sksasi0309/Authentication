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
            email=document.getElementById("email").value;
            password=document.getElementById("password").value;
            if(email=="")
            {
                alert("pleace fill the email");
                return false
            }
            else if(password=="")
            {
                alert("pleace fill the password");
                return false
            }
        }