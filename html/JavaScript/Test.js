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
        raise('presentation_prepa', 1)
    });

    $('#eve_soda').on('click', function() {
        console.log("click 2");
        raise('Presentation_filiere', 1)
    });
  
});
