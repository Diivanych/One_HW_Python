// // let namePeople = "Роза";
// // alert(`Привет, ${namePeople} !!!`);

// let element = document.getElementById("el1");
// console.log(element);
// // Добавили класс
// element.classList.add('active');
// // Удалили класс
// element.classList.remove('active');

let count = 0;
function changeColor() {

    let box = document.getElementsByClassName('box');
//    console.log(box[0]);
    let element = box[0]
    if (count % 2 == 0) {
        element.classList.add('activeBox');
    }
    else {
        element.classList.remove('activeBox');
    }
    count ++;
//    alert(`Всем привет!`);
}

let btn = document.getElementById('btn');
console.log(btn);
btn.addEventListener('click', changeColor)