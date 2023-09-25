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
      unameError.textContent = "Invalid name (only alphabetic characters allowed, minimum 3 characters)";
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

// function to validate house name
function validatePlacename() {
  const unameInput = document.getElementById("place");
  const unameError = document.getElementById("p-error");
  
  const nameRegex = /^[A-Za-z][A-Za-z ]*$/;
  
  if (!nameRegex.test(unameInput.value)) {
      unameError.textContent = "Invalid place name (only alphabetic characters, minimum length 1 alphabet, and must start with an alphabet)";
      return false
  } else {
    console.log("shnamed")
      unameError.textContent = "";
      return true
  }
}

// report validation
function validateReport() {
  const reportTextarea = document.getElementById("report");
  const reportError = document.getElementById("report-error");
  
  // Remove leading and trailing whitespaces for validation
  const reportValue = reportTextarea.value;
  
  // Check if the report has at least 300 characters
  if (reportValue.length < 300) {
    reportError.textContent = "Report must contain at least 300 characters.";
    return false;
  }

  // Remove leading and trailing whitespaces and check the length
  const trimmedReport = reportValue.trim();
  if (trimmedReport.length !== reportValue.length) {
    reportError.textContent = "Report should not start or end with whitespace.";
    return false;
  }

  // If all conditions pass, the report is valid
  reportError.textContent = "";
  return true;
}
// heading validatio
function validateHeading() {
  const headingInput = document.getElementById("heading");
  const headingError = document.getElementById("heading-error");
  
  // Remove leading and trailing whitespaces for validation
  const headingValue = headingInput.value;
  
  // Check if the heading has at least 1 character and doesn't start or end with whitespace
  if (headingValue.length < 1 || headingValue.trim() !== headingValue) {
    headingError.textContent = "Invalid heading (at least 1 character, no leading or trailing whitespace)";
    return false;
  }

  // If all conditions pass, the heading is valid
  headingError.textContent = "";
  return true;
}


function validateAllInputReport(event) {
  event.preventDefault(); // Prevent the default form submission

  if (validateFullname() && validatePlacename() && validateReport() && validateHeading()) {
      // All validations passed, allow form submission
      console.log("submitted")
      document.getElementById("report-form").submit(); // Submit the form
  } else {
    console.log("not submitted")
      // At least one validation failed, display an error message or handle it accordingly
  }
}





// // validate Title for question field in career forum
// function validateTitle() {
//   const unameInput = document.getElementById("questionTitle");
//   const unameError = document.getElementById("title-error");

//   const nameRegex = /^(?!\s)[A-Za-z\s]{3,}(?<!\s)$/;

//   if (!nameRegex.test(unameInput.value)) {
//       unameError.textContent = "Invalid Title (only alphabetic characters allowed, minimum 3 characters)";
//       return false
//   } else {
//       unameError.textContent = "";
//       return true
//   }
// }

// // validate AdditionalDetails for question field in career forum
// function validateAdditionalDetails() {
//   const unameInput = document.getElementById("additionalDetails");
//   const unameError = document.getElementById("adddetails-error");

//   const nameRegex = /^(?!\s)[\s\S]*\S$/;

//   if (!nameRegex.test(unameInput.value)) {
//       unameError.textContent = "Additional Description must contain at least 3 characters.";
//       return false
//   } else {
//       unameError.textContent = "";
//       return true
//   }
// }


// // validate detailed description in career forum
// function validateDescription() {
//   const reportTextarea = document.getElementById("questionDescription");
//   const reportError = document.getElementById("description-error");
  
//   // Remove leading and trailing whitespaces for validation
//   const reportValue = reportTextarea.value.trim();
  
//   // Check if the report has at least 150 characters
//   if (reportValue.length < 150) {
//     reportError.textContent = "Description must contain at least 150 characters.";
//     return false;
//   } else {
//     reportError.textContent = ""; // Clear the error message
//     return true;
//   }
// }




// function validateQuestionForm(event) {
//   event.preventDefault(); // Prevent the default form submission

//   if (validateTitle() && validateDescription() && validateAdditionalDetails()){
//       // All validations passed, allow form submission
//       document.getElementById("askQuestionForm").submit(); // Submit the form
//   } else {
//       // At least one validation failed, display an error message or handle it accordingly
//       console.log("Validation failed");
//   }
// }




// validate Title for question field in career forum
function validateTitle() {
  const unameInput = document.getElementById("questionTitle");
  const unameError = document.getElementById("title-error");

  const nameRegex = /^(?!\s)[A-Za-z\s]{3,}(?<!\s)$/;

  if (!nameRegex.test(unameInput.value)) {
      unameError.textContent = "Invalid Title (only alphabetic characters allowed, minimum 3 characters)";
      return false;
  } else {
      unameError.textContent = "";
      return true;
  }
}

// validate AdditionalDetails for question field in career forum (optional)
function validateAdditionalDetails() {
  const unameInput = document.getElementById("additionalDetails");
  const unameError = document.getElementById("adddetails-error");

  // Check if the input has a value
  if (unameInput.value.trim() === "") {
    // No value provided, no need to validate
    unameError.textContent = "";
    return true;
  }

  // Validate if there's a value
  const nameRegex = /^(?!\s)[\s\S]*\S$/;

  if (!nameRegex.test(unameInput.value)) {
      unameError.textContent = "Additional Description must contain at least 3 characters.";
      return false;
  } else {
      unameError.textContent = "";
      return true;
  }
}

// validate detailed description in career forum
function validateDescription() {
  const reportTextarea = document.getElementById("questionDescription");
  const reportError = document.getElementById("description-error");
  
  // Remove leading and trailing whitespaces for validation
  const reportValue = reportTextarea.value.trim();
  
  // Check if the report has at least 150 characters
  if (reportValue.length < 150) {
    reportError.textContent = "Description must contain at least 150 characters.";
    return false;
  } else {
    reportError.textContent = ""; // Clear the error message
    return true;
  }
}

function validateQuestionForm(event) {
  event.preventDefault(); // Prevent the default form submission

  if (validateTitle() && validateDescription() && validateAdditionalDetails()){
      // All validations passed, allow form submission
      document.getElementById("askQuestionForm").submit(); // Submit the form
  } else {
      // At least one validation failed, display an error message or handle it accordingly
      console.log("Validation failed");
  }
}

