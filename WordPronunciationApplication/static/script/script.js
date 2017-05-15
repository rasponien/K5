/**
 * Created by carlcustav on 5/14/2017.
 */
var app = angular.module('pronunciationWordApp', ['ngRoute']);


app.run(function ($rootScope) {

    $rootScope.words = [];
    $rootScope.feedbackInfo = "";


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
                console.log($scope.getWords())
            },
            function error(response) { console.log("SearchFrom Error"); })
    };
    $scope.addNewWord = function(event) {
        new_word = $("#uploadedWord").val();
        new_word_file = $("#uploadedFile").val();
        force = ($("#force").is(":checked")) ? "on" : "off";
        console.log(force)
        if (new_word.length === 0 || new_word_file.length === 0) return;
        console.log(new_word)
        console.log(new_word_file)
        event.preventDefault();
        $http({
            method: "POST",
            url: "upload/",
            contentType: "text/html",
            data: {
                word: new_word,
                pronunciation: new_word_file,
                force: force
            }
        }).then(
            function success(response) {
                console.log(response["data"]["msg"])
                $scope.setFeedbackInfo(response["data"]["msg"]);
            },
            function error(response) { console.log("SearchFrom Error"); })
    }

    
    $scope.playMusic = function(id) {
        console.log(id)
        new Audio("sound/?id=" + id).play()
    }

    $scope.hasNoResults = function() {
        return ($scope.getWordsLength() == 0 && !$("#searchPronunciationWord").val()) || $scope.getWordsLength() == 0;
    }


    $scope.setWords = function (pronunciationWords) {$rootScope.words = pronunciationWords;}
    $scope.getWords = function () {return $rootScope.words;}

    $scope.getWordsLength = function () {return Object.keys($scope.getWords()).length;}

    $scope.setFeedbackInfo = function (feedbackInfo) {$rootScope.feedbackInfo = feedbackInfo;}
    $scope.getFeedbackInfo = function () {return $rootScope.feedbackInfo;}

});


