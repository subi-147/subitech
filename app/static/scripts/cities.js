var state_arr = new Array( "Andhra Pradesh", "Karnataka", "Kerala", "Puducherry", "Tamil Nadu");

var s_a = new Array();
s_a[0]="";
s_a[1]=" Anantapur | Chittoor | East Godavari | Guntur | West Godavari | Kadapa |  Krishna | Nellore | Prakasam | Srikakulam  |  Visakhapatanam | Vizianagaram  ";
s_a[2]="Bangalkot | Bangalore  | Belgaum  | Bellary  | Bengaluru urban  | Bidar | Bijapur | Chamarajanagar | Chikballapur | Chikmagalur | Chitradurga | Dakshin Kannad | Davangere  | Dharwad | Gadag | Gulbarga | Hassan | Haveri | Kodagu | Kolar | Koppal | Mandya | Mysore | Raichur | Ramanagara | Shimoga | Tumkur | Udupi | Uttar Kannad | Yadgir ";
s_a[3]=" Alappuzha | Ernakulam | Idukki  | Kannur  | Kasaragode | Kollam | Kottayam | Kozhikode | Malappuram  | Palakkad | Pathanamthitta | Thiruvananthapuram |  Thrissur | Wayanad ";
s_a[4]=" Karaikal | Mahe | Pondicherry | Yanam ";
s_a[5]=" Ariyalur | Chennai | Coimbatore | Cuddalore | Dharmapuri | Dindigul | Erode | Kanchipuram | Kanniyakumari | Karur | Krishnagiri | Madurai | Nagapattinam | Namakkal | Perambalur | Pudukkottai | Ramanathapuram | Salem | Sivaganga | Thanjavur | Theni | Tiruvallur | Tiruvarur | Tiruchirappalli | Tirunelveli | Tiruppur | Tiruvannamalai | Tuticorin | Vellore | Villupuram | Virudhunagar ";

function print_state(state_id){
	// given the id of the <select> tag as function argument, it inserts <option> tags
	var option_str = document.getElementById(state_id);
	option_str.length=0;
	option_str.options[0] = new Option('Select State','');
	option_str.selectedIndex = 0;
	for (var i=0; i<state_arr.length; i++) {
		option_str.options[option_str.length] = new Option(state_arr[i],state_arr[i]);
	}
}

function print_city(city_id, city_index){
	var option_str = document.getElementById(city_id);
	option_str.length=0;	// Fixed by Julian Woods
	option_str.options[0] = new Option('Select City','');
	option_str.selectedIndex = 0;
	var city_arr = s_a[city_index].split("|");
	for (var i=0; i<city_arr.length; i++) {
		option_str.options[option_str.length] = new Option(city_arr[i],city_arr[i]);
	}
}
