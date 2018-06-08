$(document).ready(function () {
	session = new QiSession();
	$('#page_3').show();
	$('#page_01').hide();
	$('#page_0').hide();
	$('#page_1').hide();
	$('#page_2').hide();
	$('#page_eti').hide();
	$('#page_00').hide();
	$('#Translate_Java').hide();
	$('#page_irc').hide();
	$('#page_cgp').hide();

    session.service("ALMemory").done(function(ALMemory) {

        ALMemory.subscriber("accueil").done(function(subscriber) {

            subscriber.signal.connect(function() {
                $('#page_00').show();
                $('#page_0').hide();
		$('#page_01').hide();
		$('#page_1').hide();
		$('#page_2').hide();
		$('#page_3').hide();
		$('#Translate_Java').hide();
		$('#page_irc').hide();
		$('#page_eti').hide();
		$('#page_cgp').hide();

            });

        });
	ALMemory.subscriber("accueil_0").done(function(subscriber) {

            subscriber.signal.connect(function() {
                $('#page_0').show();
                $('#page_00').hide();
		$('#page_01').hide();
		$('#page_1').hide();
		$('#page_2').hide();
		$('#page_3').hide();
		$('#Translate_Java').hide();
		$('#page_irc').hide();
		$('#page_eti').hide();
		$('#page_cgp').hide();
            });

        });

        ALMemory.subscriber("presentation_prepa").done(function(subscriber) {

            subscriber.signal.connect(function() {
                $('#page_1').show();
                $('#page_0').hide();
		$('#page_01').hide();
		$('#page_00').hide();
		$('#page_2').hide();
		$('#page_3').hide();
		$('#Translate_Java').hide();
		$('#page_irc').hide();
		$('#page_eti').hide();
		$('#page_cgp').hide();
            });
        });

        ALMemory.subscriber("choix").done(function(subscriber) {

            subscriber.signal.connect(function() {
                $('#page_01').show();
                $('#page_0').hide();
		$('#page_1').hide();
		$('#page_00').hide();
		$('#page_2').hide();
		$('#page_3').hide();
		$('#Translate_Java').hide();
		$('#page_irc').hide();
		$('#page_eti').hide();
		$('#page_cgp').hide();
            });
        });
	ALMemory.subscriber("Presentation_filiere").done(function(subscriber) {

	      subscriber.signal.connect(function() {
		$('#page_2').show();
		$('#page_0').hide();
		$('#page_00').hide();
		$('#page_01').hide();
		$('#page_1').hide();
		$('#page_3').hide();
		$('#Translate_Java').hide();
		$('#page_irc').hide();
		$('#page_eti').hide();
		$('#page_cgp').hide();
		    });
		});

	ALMemory.subscriber("Presentation_filiere1").done(function(subscriber) {

	      subscriber.signal.connect(function() {
		$('#page_3').show();
		$('#page_0').hide();
		$('#page_00').hide();
		$('#page_01').hide();
		$('#page_1').hide();
		$('#page_2').hide();
		$('#Translate_Java').hide();
		$('#page_irc').hide();
		$('#page_eti').hide();
		$('#page_cgp').hide();
		    });
		});

	ALMemory.subscriber("translate").done(function(subscriber) {
	
	      subscriber.signal.connect(function() {
		
		$('#page_eti').show();
		$('#page_0').hide();
		$('#page_00').hide();
		$('#page_01').hide();
		$('#page_1').hide();
		$('#Translate_Java').hide();
		$('#page_irc').hide();
		$('#page_3').hide();
		$('#page_cgp').hide();
		});
ALMemory.subscriber("page_irc").done(function(subscriber) {
	
	      subscriber.signal.connect(function() {
		
		$('#page_irc').show();
		$('#page_eti').hide();
		$('#page_cgp').hide();
		$('#Translate_Java').hide();
		$('#page_0').hide();
		$('#page_00').hide();
		$('#page_01').hide();
		$('#page_1').hide();
		$('#page_2').hide();
		$('#page_3').hide();
		    });
		});
ALMemory.subscriber("page_cgp").done(function(subscriber) {
	
	      subscriber.signal.connect(function() {
		$('#page_cgp').show();
		$('#page_irc').hide();
		$('#page_eti').hide();
		$('#Translate_Java').hide();
		$('#page_0').hide();
		$('#page_00').hide();
		$('#page_01').hide();
		$('#page_1').hide();
		$('#page_2').hide();
		$('#page_3').hide();
		    });
		});

	ALMemory.subscriber("Translate_vers_Java").done(function(subscriber) {
            subscriber.signal.connect(function() {
		RobotUtils.onService(function(ALMemory) {
                ALMemory.getData("Translate_vers_Java").then(function(var_TextTraduit) {
                  	document.getElementById("Text_traduit").innerHTML =var_TextTraduit;
               		});
              	});
   		$('#Translate_Java').show();
		$('#page_eti').hide();
		$('#page_0').hide();
		$('#page_00').hide();
		$('#page_01').hide();
		$('#page_1').hide();
		$('#page_2').hide();
		$('#page_3').hide();
		$('#page_irc').hide();
		$('#page_cgp').hide();
            });
        });

    });

    function raise(event, value) {
        session.service("ALMemory").done(function(ALMemory) {
            ALMemory.raiseEvent(event, value);
        });
    }

    $('#translate_vers_python').on('click', function() {
        console.log("button_translate");
	var element = document.getElementById("phrase_a-traduire")
	var monTexte = element.innerText || element.textContent
        raise('translate',monTexte)
    });

    $('#tablette_vers_page3').on('click', function() {
        console.log("click 1");
        raise('Presentation_filiere1', 1)
    });

    $('#eti').on('click', function() {
        console.log("click 2");
        raise('translate', 1)
    });

    $('#cgp').on('click', function() {
        console.log("click 3");
        raise('page_cgp', 1)
    });

    $('#irc').on('click', function() {
        console.log("click 4");
        raise('page_irc', 1)
    });

    
});
