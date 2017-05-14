/**
 * Created by carlcustav on 5/14/2017.
 */
var app = angular.module('pronunciationWordApp', ['ngRoute']);


app.controller('pronunciationWordController', function ($scope, $http, $rootScope, $location) {

    $scope.getPronunciationWords = function (event) {
        event.preventDefault();
        $http({
            method: "GET",
            url: "words/" + $("#searchPronunciationWord").val()
        }).then(
            function success(response) {
                console.log("tere");
            },
            function error(response) { alert("SearchFrom Error"); })
    }
});





function playMusic(elementClass) {
    $("."+elementClass)[0].play()
}

