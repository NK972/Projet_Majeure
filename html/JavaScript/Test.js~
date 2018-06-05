$(document).ready(function () {
    session = new QiSession();

    $('#page_0').show();
    $('#page_1').hide();
    $('#page_2').hide();
	


    session.service("ALMemory").done(function(ALMemory) {

        ALMemory.subscriber("accueil_0").done(function(subscriber) {

            subscriber.signal.connect(function() {
                $('#page_0').show();
                $('#page_1').hide();
                $('#page_2').hide();
            });
        });


        ALMemory.subscriber("presentation_prepa").done(function(subscriber) {

            subscriber.signal.connect(function() {
                $('#page_1').show();
                $('#page_0').hide();
                $('#page_2').hide();

            });
        });

	ALMemory.subscriber("Presentation_filiere").done(function(subscriber) {

		    subscriber.signal.connect(function() {
		        $('#page_2').show();
		        $('#page_0').hide();
			   $('#page_1').hide();

		    });
		});


    });

    function raise(event, value) {
        session.service("ALMemory").done(function(ALMemory) {
            ALMemory.raiseEvent(event, value);
        });
    }

    $('#page_01').on('click', function() {
        console.log("click 0");
        raise('eve_vers_commande', 1)
    });

    $('#eve_eau').on('click', function() {
        console.log("click 1");
        raise('eve_commande_eau', 1)
    });

    $('#eve_soda').on('click', function() {
        console.log("click 2");
        raise('eve_commande_soda', 1)
    });

    $('#eve_biere').on('click', function() {
        console.log("click 3");
        raise('eve_commande_biere', 1)
    });

    $('#eve_orange').on('click', function() {
        console.log("click 4");
        raise('eve_commande_orange', 1)
    });

    $('#eve_cocktail').on('click', function() {
        console.log("click 5");
        raise('eve_commande_cocktail', 1)
    });

    $('#eve_gazeuse').on('click', function() {
        console.log("click 6");
        raise('eve_commande_gazeuse', 1)
    });
  $('#eve_vodka').on('click', function() {
        console.log("click 7");
        raise('eve_commande_vodka', 1)
    });


  $('#eve_wisky').on('click', function() {
        console.log("click 8");
        raise('eve_commande_wisky', 1)
    });


  $('#eve_pomme').on('click', function() {
        console.log("click 9");
        raise('eve_commande_pomme', 1)
    });



});
