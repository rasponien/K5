/**
 * Created by carlcustav on 5/14/2017.
 */
var app = angular.module('pronunciationWordApp', ['ngRoute']);


app.run(function ($rootScope) {

    $rootScope.words = [];

});

app.config(function ($routeProvider, $locationProvider) {

    $locationProvider.hashPrefix('');
    $routeProvider
        .when("/search", {
            templateUrl: "/static/angular_templates/search.html",
            controller: 'pronunciationWordController'
        }).when("/upload", {
            templateUrl: "/static/angular_templates/upload.html",
            controller: 'pronunciationWordController'
        })
        .otherwise({
            redirectTo: '/'
        });
});


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
                $scope.setWords(response["data"]);
                console.log(Object.keys($scope.getWords()).length)
            },
            function error(response) { console.log("SearchFrom Error"); })
    };
    $scope.playMusic = function(id) {
        console.log("tere");
        console.log(id);
        new Audio(id).play();
        //$("#audio" + id.toString())[0].play()
    }

    $scope.setWords = function (pronunciationWords) {$rootScope.words = pronunciationWords;}
    $scope.getWords = function () {return $rootScope.words;}
    $scope.getWordsLength = function () {return Object.keys($scope.getWords()).length;}

});


