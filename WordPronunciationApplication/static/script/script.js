/**
 * Created by carlcustav on 5/14/2017.
 */
var app = angular.module('pronunciationWordApp', ['ngRoute']);


app.controller('pronunciationWordController', function ($scope, $http, $rootScope, $location) {
    $scope.words = [];
    $scope.getPronunciationWords = function (event) {
        query_word = $("#searchPronunciationWord").val();
        if (query_word.length === 0) return;
        event.preventDefault();
        $http({
            method: "GET",
            url: "words/" + query_word
        }).then(
            function success(response) {
                //console.log(response["data"]);
               /* for (key in response["data"]){
                    $scope.words.push({key: response["data"][key]})
                }*/
                $scope.words = response["data"];
            },
            function error(response) { console.log("SearchFrom Error"); })
    };
    
    $scope.playMusic = function(id) {
        new Audio("sound/?id=" + id).play()
    }
});


