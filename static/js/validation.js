function validateFirstname() {
  const unameInput = document.getElementById("fname");
  const unameError = document.getElementById("fn");

  
   const nameRegex = /^[A-Za-z]{3,}$/; // At least 3 alphabetic characters

  if (!nameRegex.test(unameInput.value)) {
      unameError.textContent = "Invalid name (only alphabetic characters sss allowed, minimum 3 characters)";
      return false
  } else {
    console.log("fname ")
      unameError.textContent = "";
      return true
  }
}



// Function to validate middle name
// function validateMiddlename() {
//   const unameInput = document.getElementById("Mname");
//   const unameError = document.getElementById("Mn");
  
//   const nameRegex = /^[A-Za-z]+$/;
  
//   if (!nameRegex.test(unameInput.value)) {
//       unameError.textContent = "Invalid name (only alphabetic characters allowed, minimum 1 character)";
//       return false
//   } else {
//       unameError.textContent ="";
//       unmaeInput.classList.remove("is-invalid");
//       return true
//   }
// }

function validateMiddlename() {
  const unameInput = document.getElementById("Mname");
  const unameError = document.getElementById("Mn");
  
  const nameRegex = /^[A-Za-z]+$/;
  
  if (!unameInput.value) {
    // Input is null or empty, so remove the error message
    unameError.textContent = "";
    unameInput.classList.remove("is-invalid");
    return true; // No error
  } else if (!nameRegex.test(unameInput.value)) {
    console.log("mname")
    unameError.textContent = "Invalid name (only alphabetic characters allowed, minimum 1 character)";
    return false; // Error
  } else {
    unameError.textContent = "";
    unameInput.classList.remove("is-invalid");
    return true; // No error
  }
}




// function to validate Lastname
function validateLastname() {
  const unameInput = document.getElementById("lname");
  const unameError = document.getElementById("ln");
  
  const nameRegex = /^[A-Za-z]+$/;
  
  if (!nameRegex.test(unameInput.value)) {
      unameError.textContent = "Invalid input (only alphabetic characters allowed, minimum 1 character)"
      return false
  } else {
    console.log("lname")
    unameError.textContent = "";
    return true
  }
}



// function to validate house name
function validateHousename() {
  const unameInput = document.getElementById("Hname");
  const unameError = document.getElementById("Hn");
  
  const nameRegex = /^[A-Za-z][A-Za-z ]*$/;
  
  if (!nameRegex.test(unameInput.value)) {
      unameError.textContent = "Invalid name (only alphabetic characters, minimum length 1 alphabet, and must start with an alphabet)";
      return false
  } else {
    console.log("shnamed")
      unameError.textContent = "";
      return true
  }
}

// function to validate age and dob

function calculateAge(dateOfBirth) {
  const dob = new Date(dateOfBirth);
  const currentDate = new Date();
  const age = currentDate.getFullYear() - dob.getFullYear();
  const monthDiff = currentDate.getMonth() - dob.getMonth();

  if (monthDiff < 0 || (monthDiff === 0 && currentDate.getDate() < dob.getDate())) {
      return age - 1;
  }

  return age;
}

function validateDateOfBirth() {
  const dobInput = document.getElementById("dob");
  const dobError = document.getElementById("dob-error");

  const dobValue = dobInput.value;
  const age = calculateAge(dobValue);

  if (age <= 15 || age >= 30) {
      dobError.textContent = "Age must be between 15 and 30 years.";
      dobInput.classList.add("is-invalid");
      console.log("age")
      return false
  } else {
      dobError.textContent = "";
      dobInput.classList.remove("is-invalid");
      return true
  }
}


// Function to validate mobile number
function validatePhone() {
    const phoneInput = document.getElementById("mob");
    const phoneError = document.getElementById("ph");
    
    const phoneRegex = /^[0-9]{10}$/;
    
    if (!phoneRegex.test(phoneInput.value)) {
        
        phoneError.textContent = "Invalid mobile number (10 digits, no alphabets or special characters)";
        console.log("phone")
        return false
    } else {
        phoneError.textContent = "";
        return true
    }
}

// Function to validate email
function emailValidate() {
    const emailInput = document.getElementById("email");
    const emailError = document.getElementById("email-error");
    
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    
    if (!emailRegex.test(emailInput.value)) {
        emailError.textContent = "Invalid email format";
        console.log("email")
        return false
    } else {
        emailError.textContent = "";
        return true
    }
}

function validateCpwd() {
    var cpwd = document.getElementById("cpassw").value;
    var pwd = document.getElementById("password").value;
    if (pwd!==cpwd) {
      document.getElementById("cpw").innerHTML = "Password not Matched";
      console.log("cpwd")
          return false;
    } else {
      document.getElementById("cpw").innerHTML = "";
          return true;
    }
  }

  const passwordValidate = () => {
    console.log("pass");
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

function checkall(event) {
    event.preventDefault(); // Prevent the default form submission

    if (validateFirstname() && validateMiddlename() && validateLastname() && validateHousename() &&
        validateDateOfBirth() && emailValidate() && passwordValidate() && validateCpwd() && validatePhone()) {
        // All validations passed, allow form submission
        document.getElementById("reg").submit(); // Submit the form
    } else {
      console.log("sdfsd")
        // At least one validation failed, display an error message or handle it accordingly
    }
}


// validate fullname
function validateFullname() {
  const unameInput = document.getElementById("funame");
  const unameError = document.getElementById("fun");

  const nameRegex = /^(?!\s)[A-Za-z\s]+(?<!\s)$/;

  if (!nameRegex.test(unameInput.value)) {
      unameError.textContent = "Invalid name (only alphabetic characters sss allowed, minimum 3 characters)";
      return false
  } else {
      unameError.textContent = "";
      return true
  }
}

// validate age
function validateAge() {
  const ageInput = document.getElementById("age");
  const ageError = document.getElementById("age-error");
  
  const age = parseInt(ageInput.value);

  if (isNaN(age) || age < 18 || age > 60) {
    ageError.textContent = "Age must be between 18 and 60 years.";
    return false
  } else {
    ageError.textContent = "";
    return true
  }
}

function validateAll(event) {
  event.preventDefault(); // Prevent the default form submission

  if (validateFullname() && validateAge() && validatePhone()) {
      // All validations passed, allow form submission
      document.getElementById("donor").submit(); // Submit the form
  } else {
    console.log("sdfsd")
      // At least one validation failed, display an error message or handle it accordingly
  }
}

function validateAllInput(event) {
  event.preventDefault(); // Prevent the default form submission

  if (validateFullname() && validateHousename() && validatePhone()) {
      // All validations passed, allow form submission
      document.getElementById("directory").submit(); // Submit the form
  } else {
    console.log("sdfsd")
      // At least one validation failed, display an error message or handle it accordingly
  }
}