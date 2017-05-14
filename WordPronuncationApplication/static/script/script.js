/**
 * Created by carlcustav on 5/14/2017.
 */
function playMusic(elementClass) {
    $("."+elementClass)[0].play()
}

//$("#searchPronunciationWordForm").submit(searchPronunciationWords);


function searchPronunciationWords(event) {
    event.preventDefault();
    param = {
        "url"   : "words/",
        "data"  : {
            searchWord : $("#searchWord").val(),
        },
        "success": function (response) {
            console.log(response)
        }
    };
    $.ajax(param);
}