/**
 * Created by carlcustav on 5/14/2017.
 */
var app = angular.module('pronunciationWordApp', ['ngRoute']);


app.controller('pronunciationWordController', function ($scope, $http, $rootScope, $location) {
    $scope.words = [];
    $scope.getPronunciationWords = function (event) {
        console.log("words/" + $("#searchPronunciationWord").val());
        event.preventDefault();
        $http({
            method: "GET",
            url: "words/" + $("#searchPronunciationWord").val()
        }).then(
            function success(response) {
                //console.log(response["data"]);
               /* for (key in response["data"]){
                    $scope.words.push({key: response["data"][key]})
                }*/
                $scope.words = response["data"];
                console.log($scope.words)
            },
            function error(response) { console.log("SearchFrom Error"); })
    }
});





function playMusic(id) {
    $("#audio" + id).play()
}