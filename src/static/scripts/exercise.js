// querySelector is used to select the first element that matches the specified selector
// querySelector(selector)  #id, .class name, element(p,h1,img,button,small..) is used as selectors

const myHeading = document.querySelector("h1");
let myButton = document.querySelector("button");

function setUserName() {
  //This prompt() function does more than alert(), asking the user to enter data, and storing it in a variable after the user clicks OK
  const myName = prompt("Please enter your name.");

  if (!myName) {
    setUserName();
  } else {
    //localStorage.setItem() function is used to create and store a data item called 'name', setting its value to the myName variable
    localStorage.setItem("name", myName);
    myHeading.textContent = `hi, ${myName}`;
  }
}

const item = localStorage.getItem("name");
if (!item) {
  setUserName();
} else {
  const storedName = localStorage.getItem("name");
  myHeading.textContent = `Mozilla is cool, ${storedName}`;
}

// const myImage = document.querySelector("img");

// myImage.onclick = () => {
//   // attribute(src, href)
//   const mySrc = myImage.getAttribute("src");
//     console.log('hi');
//   if (mySrc === "images/product_pics/cheese.webp") {
//     myImage.setAttribute("src", "images/product_pics/apple.webp");
//   } else {
//     myImage.setAttribute("src", "images/product_pics/cheese.webp");
//   }
// };


const select = document.querySelector('#weather');
const para = document.querySelector('p');

select.addEventListener('change', setWeather);

function setWeather() {
    // access the options value in select
  const choice = select.value;

  if (choice === 'sunny') {
    para.textContent = 'It is nice and sunny outside today. Wear shorts! Go to the beach, or the park, and get an ice cream.';
  } else if (choice === 'rainy') {
    para.textContent = 'Rain is falling outside; take a rain coat and an umbrella, and don\'t stay out for too long.';
  } else if (choice === 'snowing') {
    para.textContent = 'The snow is coming down — it is freezing! Best to stay in with a cup of hot chocolate, or go build a snowman.';
  } else if (choice === 'overcast') {
    para.textContent = 'It isn\'t raining, but the sky is grey and gloomy; it could turn any minute, so take a rain coat just in case.';
  } else {
    para.textContent = '';
  }
}


const select2 = document.querySelector('#theme')
const html = document.querySelector('body')


function update(bgColor, textColor) {
    html.style.backgroundColor = bgColor;
    html.style.color = textColor;
  }

select2.addEventListener('change', () => select2.value === 'black'
  ? update('#2C3333', 'white')
  : update('white', '#2C3333')
);  


const select_calendar = document.querySelector('#cal');
const list = document.querySelector('ul');
const h1 = document.querySelector('#month');


select_calendar.addEventListener('change', () => {
    const choice = select_calendar.value;
  
    let days = 31;
    if (choice === 'feb') {
      days = 28;
    } else if (choice === 'april' || choice === 'june' || choice === 'aug'|| choice === 'sep') {
      days = 30;
    }
  
    createCalendar(days, choice);
  });
    

function createCalendar(days, choice) {
    list.innerHTML = '';
    h1.textContent = choice;
    for (let i = 1; i <= days; i++) {
        // create li inside ul
      const listItem = document.createElement('li');

      listItem.style.backgroundColor = 'green'
      listItem.style.margin = "10px"
      listItem.style.padding = "10px"
      listItem.style.width = "200px"
      listItem.style.listStyleType = "None"
      
      listItem.textContent = i;
      list.appendChild(listItem);
    }
  }
  
  createCalendar(31,'January');



  
  const cats = ['Leopard', 'Serval', 'Jaguar', 'Tiger', 'Caracal', 'Lion'];
  
  const upperCats = cats.map((string)=>{
    return string.toUpperCase();
  });
  
  // [ "LEOPARD", "SERVAL", "JAGUAR", "TIGER", "CARACAL", "LION" ]

  
  // accessing array value by for in loop
  function data(){
   
    for (i in cats) {
        const value = cats[i].toUpperCase()
    console.log(value);
    }
    
  }  


  
  const catss = ['Leopard', 'Serval', 'Jaguar', 'Tiger', 'Caracal', 'Lion'];
  
  const filtered = catss.filter((cat)=>{
    return cat.startsWith('L');
  });
  
  // [ "Leopard", "Lion" ]

  
  const catsz = ['Pete', 'Biggles', 'Jasmine'];

let myFavoriteCats = 'My cats are called ';

for (let i = 0; i < catsz.length; i++) {
  if (i === catsz.length - 1) {   // We are at the end of the array
    myFavoriteCats += `and ${catsz[i]}.`
  } else {
    myFavoriteCats += `${catsz[i]}, `
  }
}




const contacts = ['Chris:2232322', 'Sarah:3453456', 'Bill:7654322', 'Mary:9998769', 'Dianne:9384975'];
const para2 = document.querySelector('#srch');
const input = document.querySelector('#srh');
const btn = document.querySelector('#search');

btn.addEventListener('click', () => {
   
  const searchName = input.value.toLowerCase();
  input.value = '';
  input.focus();
  para2.textContent = '';
  for (const contact of contacts) {
    const splitContact = contact.split(':');
    if (splitContact[0].toLowerCase() === searchName) {
      para2.textContent = `${splitContact[0]}'s number is ${splitContact[1]}.`;
      break;
    }
  }
  if (para2.textContent === '') {
   para2.textContent = 'Contact not found.';
 }
})


//simple interest
p = 50000
r = 12.5 
t = 2 // time or number of years(N)
// i = p * r/100 * t

// total principal = p + i
ri = r/100
N = t
T = p * (1+ri)^N
// T = 50,000 * (1+(12.5/100))^5

n1 = 365
n2 = 1


// compound interest
T1 = p * (1+(ri/n1))^(n1*t) // total value compound daily
T2 = p * (1+(ri/n2))^(n2*t) // total value compound yearly

I1 = T1-p //  interest on daily compounding
I2 = T2-p // interest on yearly compounding

console.log(T1,T2,I1,I2);



