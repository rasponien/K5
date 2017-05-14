/**
 * Created by carlcustav on 5/14/2017.
 */
function playMusic(elementClass) {
    console.log(elementClass)
    $("."+elementClass)[0].play()
}