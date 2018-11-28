(function () {
    var xhttp = new XMLHttpRequest();
    var url = 'http://localhost:8000/posts/';
    var txtData = document.getElementById('txtData');

    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var data = this.responseText;
            txtData.style.color = "black";
            txtData.innerHTML = data;
            users = JSON.parse(data);
            console.log(users);
            for (let i in users.results) {
                displayUser(users.results[i], i);
            }
        } else {
            txtData.style.color = "red";
            txtData.innerHTML = data;
        }
    };

    xhttp.open("GET", url, true);
    xhttp.send();

    if (localStorage.getItem("selectedUsers")) {
        selectedUsers = JSON.parse(localStorage.getItem("selectedUsers"));
    }
    var displayUser = function (user, i) {
        var usersContainer = document.getElementById("gallery");
        var userContainer = document.createElement("div");
        var nameContainer = document.createElement("p");
        var emailContainer = document.createElement("p");
        if (selectedUsers[i]) {
            userContainer.className = "card pink";
        } else {
            userContainer.className = "card";
        }
        userContainer.addEventListener("click", function (mouse) {
            if (!this.selected) {
                userContainer.className = "card pink";
                this.selected = true;
                selectedUsers[i] = true;
                saveData("selectedUsers", selectedUsers);
            } else {
                userContainer.className = "card";
                this.selected = false;
                selectedUsers[i] = false;
                saveData("selectedUsers", selectedUsers);
            }
            console.log("selected");
        });
        console.log(user)
        nameContainer.innerHTML = "<b>Nombre: </b>" + user.name;
        emailContainer.innerHTML = "<b>Dirección: </b>" + user.breed;
        // Add childs
        userContainer.appendChild(nameContainer);
        userContainer.appendChild(emailContainer);
        // Add to page
        usersContainer.appendChild(userContainer);
    }

    var saveData = function (key, data) {
        var toSave = JSON.stringify(data);
        localStorage.setItem(key, toSave);
    }

})();