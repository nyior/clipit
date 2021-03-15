const baseUrl = "http://shter.herokuapp.com/api/v1/";
async function postData(data) {
    const url = `${baseUrl}shortcode`;
    // const url = "http://127.0.0.1:8000/api/v1/shortcode";

    const response = await fetch(
        url, 
        {
            method: 'POST',
            credentials:"include",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        }
    );

    return response.json(); 
}


async function getUrlStats(shortcode) {
    const url = `${baseUrl}${shortcode}/stats`;

    const response = await fetch(
        url, 
        {
            method: 'GET',
            credentials:"include",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        }
    );

    return response.json(); 
}


const copyKlinLink = () => {
    let element = document.querySelector("#shortened-url");
    elementText = element.textContent;

    try {
      navigator.clipboard.writeText(elementText);

      let elem = document.querySelector("#tooltiptext");
      elem.innerHTML = "copied!"
    } catch (err) {
      alert("Oops, unable to copy");
    }
}
  
   
const urlShortener = (data) => {

    postData( data )
        .then(data => {
            originalUrl = encodeURI(data.longUrl)
            shortcode = encodeURI(data.shortcode)
            baseUrl = "https://www.clipit.fun/"
            newUrl = `www.clipit.fun/${shortcode}`
            newurlHref = baseUrl.concat(shortcode);
            trimmedUrl = String(data.longUrl)

            if(trimmedUrl.length > 10){
                trimmedUrl = trimmedUrl.substring(0, 10).concat("...");
            } 
            document.querySelector("#shortened-url").href = newurlHref;
            document.querySelector("#original-url").href = originalUrl;

            document.querySelector("#shortened-url").innerHTML = newUrl;
            document.querySelector("#original-url").innerHTML = trimmedUrl;

            let copy = document.querySelector("#klinurl-copy");
            copy.style.visibility = "visible";

            copy.addEventListener("click", (e) => {
                copyKlinLink();
            });
        });
};


const validateUrl= (url) =>{
    let pattern = /^(?:(?:https?|ftp):\/\/)?(?:(?!(?:10|127)(?:\.\d{1,3}){3})(?!(?:169\.254|192\.168)(?:\.\d{1,3}){2})(?!172\.(?:1[6-9]|2\d|3[0-1])(?:\.\d{1,3}){2})(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))|(?:(?:[a-z\u00a1-\uffff0-9]-*)*[a-z\u00a1-\uffff0-9]+)(?:\.(?:[a-z\u00a1-\uffff0-9]-*)*[a-z\u00a1-\uffff0-9]+)*(?:\.(?:[a-z\u00a1-\uffff]{2,})))(?::\d{2,5})?(?:\/\S*)?$/;
    
    return pattern.test(url);
};


const validateShortcode= (shortcode) =>{
    let condition = shortcode.length >= 4 && shortcode.length <= 31;
    return (condition ? true : false);
};


const getInputFieldCOntent = () => { 
    let longUrl = document.querySelector("#longurl").value;
    let shortcode = document.querySelector("#shortcode").value;
    
    if (shortcode && (validateUrl(longUrl) && validateShortcode(shortcode))){
        urlShortener({ "longUrl": longUrl, "shortcode": shortcode }) 
    }

    if (!shortcode && validateUrl(longUrl)) {
        urlShortener({ "longUrl": longUrl}) 
    };
};


const toggleForm = () => {
    let elements = document.querySelectorAll(".advanced");
    let regularPrompt = document.querySelector(".regular");

    for (let index = 0; index < elements.length; index++) {
        let element = elements[index];

        if (element.style.display === "none") {
            element.style.display = "block";
            regularPrompt.style.display = "none";
        } else {
            element.style.display = "none";
            regularPrompt.style.display = "block";
        }
        
    }
}


document.addEventListener("DOMContentLoaded", () => {
    let button = document.querySelector("#klinurl-button");
    let toggleButtons = document.querySelectorAll("#toggle");
    let statsLink = document.querySelectorAll("#stats-link");

    button.addEventListener("click", (e) => {
        getInputFieldCOntent()

    });

    statsLink.addEventListener("click", (e) => {
        getInputFieldCOntent()

    });

    for (let index = 0; index < toggleButtons.length; index++) {
        let element = toggleButtons[index];

        element.addEventListener("click", (e) => {
            toggleForm();
        });
        
    }  
});