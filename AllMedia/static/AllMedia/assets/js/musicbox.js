
const selectElement =(s) => document.querySelector(s);
const searchElem= document.querySelector('.search-bar');
const removeSearchElem=document.querySelector('.search-close');

// for music play struture
const toggle_btn = document.querySelector('.dropdown-btn-arrow');
const toggle_btn_down = document.querySelector('.dropdown-btn-arrow-down');

// event listener

toggle_btn.addEventListener('click', ()=>{
    selectElement('.background-wall-player').classList.add('active-background');
    selectElement('.dropdown-btn-arrow').classList.add('active');
    selectElement('.image').classList.add('active');
    selectElement('.buttons').classList.add('active');
    selectElement('.dropdown-btn-arrow').style.display='none'
})

toggle_btn_down.addEventListener('click', ()=>{
    selectElement('.background-wall-player').classList.remove('active-background');
    selectElement('.dropdown-btn-arrow').classList.remove('active');
    selectElement('.image').classList.remove('active');
    selectElement('.buttons').classList.remove('active');
    selectElement('.dropdown-btn-arrow').style.display='block'
})


// end music playing struture



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


// serach bar function

searchElem.addEventListener('click', () => {
    document.querySelector('nav').style.display="none"
    document.querySelector('.show-search').classList.add('active')
})

// remove search

removeSearchElem.addEventListener('click', () => {
    document.querySelector('nav').style.display="flex"
    document.querySelector('.show-search').classList.remove('active')
})


// .............new functionality..............
// media queries for search functionality

const searchDiv = document.querySelector('.search')

let x=window.matchMedia("(min-width:700px)");

if(x){
    myFunction(x)
    
}


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

// end of search... 

