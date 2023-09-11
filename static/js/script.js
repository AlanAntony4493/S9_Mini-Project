const emailValidate = () => {
    console.log("working");
    const email = document.getElementById("email").value;
    re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!re.test(email)) {
      document.getElementById("email-error").textContent =
        "Please enter valid email";
      return false;
    } else {
      document.getElementById("email-error").textContent = "";
      return true;
    }
  };
  
  const passwordValidate = () => {
    console.log("working");
    const pass = document.getElementById("password").value;
   // const cpass = document.getElementById("cpass").value;
  
    re = /^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$/;
    if (!re.test(pass)) {
      document.getElementById("pass-error").textContent =
        "Minimum eight characters, at least one letter, one number and one special character";
      return false;
    } else {
      document.getElementById("pass-error").textContent = "";
      return true;
    }
  };

  function validateUname() {
    var letters =/^[A-Za-z ]*$/;
    var uname = document.getElementById("fname").value;
    if ((!letters.test(uname) || uname.length <= 2) && uname.length>0) {
      document.getElementById("uc").innerHTML = "Username should only contain alphabets and be at least 3 characters long";
          return false;
    } else {
      document.getElementById("uc").innerHTML = "";
          return true;
    }
  }
  function validatePhone() {
    var ph_exp =/^\d{10}$/;
    var phone = document.getElementById("mob").value;
    if (!ph_exp.test(phone)||!(phone.length >0) && phone.length<=9 ){
      document.getElementById("ph").innerHTML = "Please enter values between 0-9 and Length should be 10 digits";
          return false;
    } else {
      document.getElementById("ph").innerHTML = "";
          return true;
    }
  }
  function validateCpwd() {
    var cpwd = document.getElementById("cpassw").value;
    var pwd = document.getElementById("password").value;
    if (pwd!==cpwd) {
      document.getElementById("cpw").innerHTML = "Password not Matched";
          return false;
    } else {
      document.getElementById("cpw").innerHTML = "";
          return true;
    }
  }
  
//   function checkall()
//   {
//     if(validateUname()&&validatePhone()&&passwordValidate()&&validateCpwd()&&emailValidate())
    
//     return true;
// else
// {
//   return false;
// }
   
//   }

  