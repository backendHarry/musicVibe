const selectElement =(s) => document.querySelector(s);
const searchElem= document.querySelector('.search-bar');
const removeSearchElem=document.querySelector('.search-close');

// hamburger menu
// function

selectElement('.open').addEventListener('click', () => {
    selectElement('.nav-list').classList.add('active');
});

// remove

selectElement('.close').addEventListener('click', () => {
    selectElement('.nav-list').classList.remove('active');
});
// hamburger end 


// search bar function

searchElem.addEventListener('click', () => {
    document.querySelector('nav').style.display="none"
    document.querySelector('.show-search').classList.add('active')
})

// remove search

removeSearchElem.addEventListener('click', () => {
    document.querySelector('nav').style.display="flex"
    document.querySelector('.show-search').classList.remove('active')
})


// code for creating files /selecting files

const fileSelector = document.getElementById('fileSelect'), 
    fileElem=document.getElementById("fileElem");

fileSelector.addEventListener("click", (e) =>{
    if(fileElem){
        fileElem.click();
    }
}, false);

// now code for adding to html list
fileElem.addEventListener('change', function(e){

    let ff=document.forms['uploadform'];
    let files = e.target.files;

    for(let i = 0, file; file = files[i]; i++){
        const fileList= this.files[i].name;
        li=document.createElement('li');
        li.className='list-item';
        // for span of text
        spanText=document.createElement('span');
        spanText.className='list-text';
        spanText.innerText=fileList;
        li.appendChild(spanText);
        // for span of Icon
        spanIcon=document.createElement('span');
        spanIcon.className='list-icon';
        // for cancel icon
        cancelIcon=document.createElement('i');
        cancelIcon.className='trash fas fa-times';
        spanIcon.appendChild(cancelIcon);
        li.appendChild(spanIcon);
        // add to ul
        ul=document.querySelector('.all-items');
        ul.appendChild(li);
    }
}, false);

// code to remove function 

ul=document.querySelector('.all-items');
ul.addEventListener('click', (e) =>{
    const item = e.target;
    if(item.classList[0] == 'trash'){
       const listItem = item.parentElement.parentElement;
       listItem.classList.add('fall')
       console.log(listItem)
       listItem.addEventListener('transitionend', (e)=>{
           listItem.remove();
       })
    }
});



// .............new functionality..............
// media queries for search functionality

const searchDiv = document.querySelector('.search')
function myFunction(x){
    if(x.matches){
        inputSearch=document.createElement('INPUT');
        inputSearch.setAttribute("type", "search");
        inputSearch.className='search-field';
        inputSearch.placeholder="search here";
        inputSearch.name="q";
        submitSearch=document.createElement('INPUT');
        submitSearch.setAttribute("type", "submit");
        submitSearch.className='submit-check';
        searchDiv.appendChild(inputSearch);
        searchDiv.appendChild(submitSearch);
    }
}


let x=window.matchMedia("(min-width:700px)");
if(x){
    myFunction(x);
}

// end of search... awesome coz it was stressfullllll