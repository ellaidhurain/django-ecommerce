let addBtn = document.getElementsByClassName("update-cart");

// add loop to get all the btn data
for (var i = 0; i < addBtn.length; i++) {
  // add event listener to button for get the product id, action, name what we are passing the data in button
  addBtn[i].addEventListener("click", function (e) {
    e.preventDefault()
    let productId = this.dataset.product;
    let action = this.dataset.action;
    let prod_name = this.dataset.prod;
    // let all = this.dataset.data-all;
    // document.getElementById("inp").innerHTML =  prod_name

    console.log("id:", productId, "action:", action, "name:", prod_name, );

    console.log(user);

    if (user === "AnonymousUser") {
      console.log("Not logged in");
    } else {
      updateUserOrder(productId, action, prod_name,);
    }
  });
}

function updateUserOrder(productId, action) {
  console.log("User is logged in, sending data..");

  var url = "/updateItem/";

  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({ productId: productId, action: action }),
  })
    .then((res) => {
      console.log(res);
      return res.json();
    })

    .then((data) => {
      console.log("data:", data);
      location.reload();
    });
}

