"use strict";

// ЭЛЕМЕНТЫ ИНТЕРФЕЙСА
const loginSection = document.querySelector(".login-section");
const mainSection = document.querySelector(".main-section");
// ЛОГИН
const loginFormSubmitButton = document.querySelector(
  ".login-form-submit-button"
);
const loginFormInputUserName = document.querySelector(
  ".login-form-input-username"
);

const loginFormInputPassword = document.querySelector(
  ".login-form-input-password"
);
const currentUser = document.querySelector(".tabs-active-user-username");
const logoutButton = document.querySelector(".tabs-active-user-logout");
// let isUserNameValid = true;
// let isPasswordValid = true;
// let isLoggedIn = true;
// let validUser = {
//   userName: ["samolet"],
//   password: ["hack"],
//   userValidation() {
//     for (let i = 0; i < validUser.userName.length; i++) {
//       if (
//         loginFormInputUserName.value.includes(validUser.userName[i]) &&
//         loginFormInputPassword.value.includes(validUser.password[i])
//       ) {
//         isUserNameValid = true;
//         isPasswordValid = true;
//         currentUser.textContent = validUser.userName[i];
//         break;
//       } else {
//         isUserNameValid = false;
//         isPasswordValid = false;
//       }
//     }
//   },
// };
// loginFormSubmitButton.addEventListener("click", function (e) {
//   e.preventDefault();
//   validUser.userValidation();
//   isUserNameValid && isPasswordValid
//     ? (isLoggedIn = true)
//     : alert("Отказано в доступе");
//   if (isLoggedIn === true) {
//     loginSection.classList.remove("active");
//     document.body.classList.remove("active");
//     mainSection.classList.add("active");
//   }
// });
// logoutButton.addEventListener("click", function () {
//   isLoggedIn = false;
//   loginSection.classList.add("active");
//   document.body.classList.add("active");
//   mainSection.classList.remove("active");
//   currentUser.textContent = "";
//   location.reload();
// });
// ТАБЫ
const tabs = document.querySelectorAll(".tabs-tab");
const tabsContent = document.querySelectorAll(".tab-content");
tabs.forEach((tab, index) => {
  tab.addEventListener("click", function () {
    tabs.forEach((tab) => tab.classList.remove("active"));
    tab.classList.add("active");
    tabsContent.forEach((content) => {
      content.classList.remove("active");
    });
    tabsContent[index].classList.add("active");
  });
});
// ФОРМА АНКЕТЫ
let isGenderValid = false;
let isSurnameValid = false;
let isNameValid = false;
let isBirthDateValid = false;
let isSalaryValid = false;
const profileForm = document.querySelector(".profile-form");
// Инпут выбора пола
const inputGenderLabel = document.querySelectorAll(
  ".tab-content-input-profile-gender-label"
);
const inputGender = document.querySelectorAll(
  ".tab-content-input-profile-gender"
);
inputGender.forEach((inputGender, index) => {
  inputGender.addEventListener("click", function () {
    inputGenderLabel.forEach((label) => label.classList.remove("active"));
    if (inputGender.checked) {
      inputGenderLabel[index].classList.add("active");
    } else {
      inputGenderLabel[index].classList.remove("active");
    }
  });
});
// Валидация инпута выбора пола
const inputGenderValidation = () => {
  inputGender.forEach((inputGender, index, inputGenders) => {
    inputGender.addEventListener("focus", function () {
      inputGenderLabel.forEach((label) => {
        label.classList.remove("invalid");
      });
    });
    if (inputGenders[0].checked || inputGenders[1].checked) {
      inputGenderLabel[index].classList.remove("invalid");
      isGenderValid = true;
    } else {
      inputGenderLabel[index].classList.add("invalid");
      isGenderValid = false;
    }
  });
};
// Инпут фамилии
const inputSurname = document.querySelector(
  ".tab-content-input-profile-surname"
);
inputSurname.addEventListener("change", function () {
  inputSurname.classList.add("valid");
  inputSurname.classList.remove("invalid");
});
// Валидация инпута фамилии
const inputSurnameValidation = () => {
  if (inputSurname.value !== "") {
    inputSurname.classList.add("valid");
    isSurnameValid = true;
  } else {
    inputSurname.classList.add("invalid");
    isSurnameValid = false;
  }
};
// Инпут имени
const inputName = document.querySelector(".tab-content-input-profile-name");
inputName.addEventListener("change", function () {
  inputName.classList.add("valid");
  inputName.classList.remove("invalid");
});
// Валидация инпута имени
const inputNameValidation = () => {
  if (inputName.value !== "") {
    inputName.classList.add("valid");
    isNameValid = true;
  } else {
    inputName.classList.add("invalid");
    isNameValid = false;
  }
};
// Инпут отчества
const middleName = document.querySelector(
  ".tab-content-input-profile-middlename"
);
// Инпут даты рождения
const inputBirthdayWrapper = document.querySelector(
  ".tab-content-input-profile-row-birthdate"
);
const inputBirthday = document.querySelector(
  ".tab-content-input-profile-birthdate"
);
inputBirthday.addEventListener("focus", function () {
  inputBirthdayWrapper.classList.remove("active");
});
inputBirthdayWrapper.addEventListener("click", function (e) {
  inputBirthday.focus();
});
inputBirthday.addEventListener("focusout", function () {
  inputBirthday.value
    ? inputBirthdayWrapper.classList.remove("active")
    : inputBirthdayWrapper.classList.add("active");
});
inputBirthday.addEventListener("change", function () {
  inputBirthday.classList.add("valid");
  inputBirthday.classList.remove("invalid");
  inputBirthday.value === ""
    ? inputBirthday.classList.add("invalid")
    : inputBirthday.classList.remove("invalid");
});
// Валидация инпута даты рождения
const inpuBirthDateValidation = () => {
  if (inputBirthday.value !== "") {
    inputBirthday.classList.add("valid");
    isBirthDateValid = true;
  } else {
    inputBirthday.classList.add("invalid");
    isBirthDateValid = false;
  }
  inputBirthday.value !== ""
    ? inputBirthdayWrapper.classList.add("valid")
    : inputBirthdayWrapper.classList.add("invalid");
};
// Инпут суммы
const inputSalary = document.querySelector(".tab-content-input-profile-salary");
inputSalary.addEventListener("change", function () {
  inputSalary.classList.add("valid");
  inputSalary.classList.remove("invalid");
});
// Валидация инпута суммы
const inputSalaryValidation = () => {
  if (inputSalary.value !== "") {
    inputSalary.classList.add("valid");
    isSalaryValid = true;
  } else {
    inputSalary.classList.add("invalid");
    isSalaryValid = false;
  }
};
// Кнопка отправки
// const profileFormSubmitButton = document.querySelector(".profile-form-submit");
// profileFormSubmitButton.addEventListener("click", function (e) {
const pf = document.querySelector(".profile-form")
pf.addEventListener("submit", (event) => {
  e.preventDefault();
  inputGenderValidation();
  inputSurnameValidation();
  inputNameValidation();
  inpuBirthDateValidation();
  inputSalaryValidation();
  if (
    !isGenderValid ||
    !isSurnameValid ||
    !isNameValid ||
    !isBirthDateValid ||
    !isSalaryValid
  ) {
    // alert("Форма отправлена");
    // inputGender.forEach((gender) => (gender.checked = false));
    // inputGenderLabel.forEach((label) => label.classList.remove("active"));
    // inputSurname.value = "";
    // inputName.value = "";
    // middleName.value = "";
    // inputBirthday.value = "";
    // inputBirthdayWrapper.classList.add("active");
    // inputBirthdayWrapper.classList.remove("invalid");
    // inputSalary.value = "";
    alert("Заполните обязательные поля");
  }
  // } else {
  //   alert("Заполните обязательные поля");
  // }
});
// ФОРМА ИМПОРТА
// const importForm = document.querySelector(".import-form");
// const importFormSubmitButton = document.querySelector(".import-form-submit");
// // Инпут с файлом
// const inputFile = document.querySelector(".tab-content-input-file");
// const inputFileText = document.querySelector(".tab-content-input-file-text");
// inputFile.addEventListener("change", function () {
//   if (inputFile.value) {
//     inputFileText.textContent = inputFile.value;
//     inputFileText.classList.remove("invalid");
//     console.log(inputFile.files[0]);
//   } else {
//     inputFileText.textContent = "допустимый формат: .csv, .xlsx";
//   }
// });
// // Валидация инпута с вайлом
// const inputFileValidation = (e) => {
//   let inputValueExtension = inputFile.value.split(".").reverse()[0];
//   const validExtesions = ["csv", "xlsx"];
//   if (validExtesions.includes(inputValueExtension)) {
//     inputFileText.classList.remove("invalid");
//     inputFileText.textContent = "допустимый формат: .csv, .xlsx";
//     inputFile.value = "";
//     alert("Форма отправлена");
//     importForm.submit();
//   } else {
//     inputFileText.classList.add("invalid");
//     if (!inputFile.value) {
//       alert("Выбирите файл");
//     } else {
//       !validExtesions.includes(inputValueExtension);
//       alert("Недопустимый формат файла");
//       inputFileText.textContent = "допустимый формат: .csv, .xlsx";
//       inputFile.value = "";
//     }
//   }
// };
// Кнопка отправки
// importFormSubmitButton.addEventListener("click", function (e) {
//   e.preventDefault();
//   inputFileValidation();
// });


// const importFormSubmitButton = document.querySelector(".import-form-submit");
// Инпут с файлом
// const inputFile = document.querySelector(".tab-content-input-file");
// const inputFileText = document.querySelector(".tab-content-input-file-text");
// inputFile.addEventListener("change", function () {
//   if (!inputFile.value) {
//     inputFileText.textContent = "допустимый формат: .csv, .xlsx";
//   }
// });

// Валидация инпута с вайлом
// const inputFileValidation = (e) => {
//   let inputValueExtension = inputFile.value.split(".").reverse()[0];
//   const validExtesions = ["csv", "xlsx"];
//   if (!validExtesions.includes(inputValueExtension)) {
//     inputFileText.classList.add("invalid");
//     if (!inputFile.value) {
//       alert("Выбирите файл");
//     } else {
//       !validExtesions.includes(inputValueExtension);
//       alert("Недопустимый формат файла");
//       inputFileText.textContent = "допустимый формат: .csv, .xlsx";
//       inputFile.value = "";
//     }
//   }
// };