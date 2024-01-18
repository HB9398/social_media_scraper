# social_media_scraper
 Used python-tweePy with the Twitter API to scrape through the global feed for tweets (refresh rates: 1500 tweets)  about locusts with pictures of proof to update a database.  This data was then plotted as a heat-map of the world. 

I have been a bit lazy while uploading this code, as it was just a passion project.
However each block of code should give similar results and please ensure enter your API keys:


{'kansas': 1, 'addis ababa': 1, 'uganda': 3, '': 264, 'kismayo, somalia': 1, 'nairobi': 1, 'montréal, canada': 1, 'kenya': 5, 'australia': 2, 'guanduanis,  guanduania': 1, 'mogadishu, somalia ': 1, 'columbus, oh': 1, 'delft, netherlands ': 1, 'somalia': 1, 'nairobi, kenya': 24, 'hrvatska': 1, 'everywhere food grows': 1, 'california, usa': 4, 'karachi': 3, 'pakpattan, pakistan': 1, 'newtonsville, oh': 1, 'sindh, pakistan': 1, 'new delhi': 14, 'ashburn': 1, 'japan': 1, 'thailand - madagascar - egypt': 1, 'united states': 18, 'findlay, oh': 1, 'calgary, alberta': 2, 'bangkok, nairobi, new york': 1, 'lesbiania': 1, 'nepal': 10, 'singapore': 4, 'melbourne': 1, 'world': 32, 'new zealand': 1, 'kampala, uganda': 2, 'gurgaon, india': 1, 'usa': 5, 'florida': 1, 'texas, usa': 3, 'alpine, ca': 1, 'ontario, canada': 2, 'versailles, france': 1, ' u.s.a 🇺🇸  #prolife  no dm': 1, "a'dam nl": 1, 'yakima washington': 1, 'detroit, michigan': 4, 'world patriot, costa rica ': 1, 'missouri, usa': 2, '👿ny👿': 1, 'america, land that i love ': 1, 'missouri, united states': 1, 'houston, tx': 3, '#ņīňĵåşƫʋƞƫɀ': 1, 'in your heart': 1, 'free & wild minnesota usa': 1, 'new york, usa': 2, 'st. paul, minnesota': 1, 'new york, ny': 13, 'bengaluru ': 1, 'brussels': 3, 'finland & global': 1, 'kimanzichana': 1, 'nj': 3, 'pakistan': 18, 'tampa, fl': 2, "beijing, people's republic of china": 1, 'panaji, goa, india': 1, 'hyderabad, india': 4, 'lake worth, fl': 1, 'everywhere': 1, 'kisumu, kenya': 2, 'nakuru, kenya': 1, 'geneva, switzerland': 1, 'spain': 1, 'machakos, kenya': 1, 'kabete, kenya': 1, 'busia': 1, 'ruiru, kenya': 1, 'hamlet, nc': 1, 'kericho, kenya': 2, 'india': 25, 'gurgaon': 1, 'new delhi, india ': 1, 'squamish, bc': 1, 'new orleans, la': 1, 'lost in the stars': 3, 'chennai, india': 4, 'chicago': 1, 'path leading to heaven': 1, 'virginia, usa': 1, 'san antonio, tx': 2, 'under the bridge': 1, 'málaga': 1, 'kingdom of saudi arabia': 1, 'africa': 5, 'canary islands, spain': 1, 'nc': 1, 'global': 1, 'belfast, northern ireland': 1, 'gurugram, delhi-ncr, india': 1, 'quetta, pakistan': 1, 'beijing': 1, 'lahore, pakistan': 4, '日本': 1, 'kenya🇰🇪': 1, 'kathmandu, nepal': 7, 'morristown, ny': 1, 'fort lauderdale, fl': 2, ' nairobi kenya': 1, 'isiolo, kenya': 1, 'dublin, ireland.': 1, 'harrow, london': 1, 'chile, santiago': 1, 'florida, usa': 1, 'hamburg, deutschland': 3, 'delhi': 1, 'islamabad': 1, 'american expat in the uae': 1, 'mumbai': 5, 'new delhi, india': 14, 'kwale & kitui counties, kenya': 1, 'ghana': 1, 'victoria, british columbia': 1, 'jupiter, fl': 1, 'melbourne vic': 1, 'texas': 1, 'michigan, usa': 1, 'blue dot-red state ': 1, 'minneapolis, mn': 1, 'sf bay': 1, 'colorado, usa': 1, 'england, uk': 1, 'the south': 1, 'chattanooga': 1, 'earth bound misfit': 1, 'shell beach, ca, usa': 1, 'chicago, il': 2, 'north carolina, usa': 2, 'granite bay, california': 1, 'sydney': 2, 'washington, dc': 4, 'somewhere north': 1, 'ireland': 1, 'san francisco, california': 1, '🗽nyc 🍎': 1, 'new delhi ': 1, 'hong kong': 2, 'searching..': 1, 'germany': 1, 'here & there @121depression': 1, 'bonn, germany': 2, 'beautiful british columbia': 1, 'berlin, deutschland': 1, 'london, england': 3, 'baltimore, md': 1, 'london': 4, 'baltimore': 1, 'brooklyn, ny': 1, 'deutschland i germany': 1, 'texas hill country 🦇': 1, 'chi-town': 1, 'seattle, wa': 1, 'ordu merkez, ordu': 1, 'olsztyn': 1, 'new jersey': 1, 'sydney, australia': 1, 'polska': 1, 'ελλάς': 1, 'twente': 1, 'somewhere in  a castle': 1, 'mumbai, india': 8, 'beijing china': 1, 'karachi, pakistan': 1, 'earth': 2, 'indore, india': 1, 'rome, italy': 1, 'karachi, pakistan ': 1, 'bhubaneshwar ': 1, 'jhumka city - banana republic': 1, 'the matrix. take the red pill. always follow the $.': 2, 'dubai, united arab emirates': 4, 'atlanta, ga': 2, 'भारत': 1, "unceded territory coast salish xʷməθk'̓wəym (musqueam) skwxwu'́7mesh (squamish) stó:lō &   sə'li'lwətaʔ/səlilwittulh̓ (tsleil- waututh)": 1, 'the vancouver model #culleniscoming #communitynotcommodity': 1, '🇬🇧london': 1, 'dublin, ga': 1, 'omnipresent when not in sheffπ': 1, 'hotel california': 1, 'kansas, usa': 1, 'united kingdom - india': 1, 'amazon.com': 1, 'bengaluru, india': 2, '#netherlands #soest - global': 1, 'vijayawada, india': 1, 'limerick, ireland': 1, 'kolkata, india': 1, 'kolkata': 1, 'hyderabad,telangana, india': 1, 'palakkad-bengaluru': 1, 'brasil': 1, 'ksa ': 1, 'jaipur, india': 3, 'siwana, rajsthan, india': 1, 'europe': 2, 'coimbatore, india': 2, 'chennai': 3, 'jaunpur, india': 1, 'on 📲 in st. albert, 🆎 🇨🇦': 1, 'leeds england uk': 1, 'uper': 1, 'odisha': 1, 'patna, india': 1, 'hyderabad': 4, 'bangalore': 4, 'mayiladuthurai': 1, 'stockholm': 2, 'kochi': 1, 'maharashtra, india': 2, 'cambridgeshire england': 1, 'washington, usa': 1, 'dubai': 2, 'orbiting nearest black hole': 1, 'scotland, united kingdom': 1, 'hillsdale, mi': 1, 'new kingstown, pa': 1, '欧州 europe': 1, 'noida, india': 1, 'republic of the philippines': 2, 'point lookout': 1, 'punjab': 1, 'united arab emirates': 1, 'pataliputra': 1, 'chicagoland': 3, 'shuttling berlin & bangalore': 1, 'tokyo, japan': 2, '千葉県': 1, 'hyderabad, telangana': 1, "i'm with elvis - everywhere": 1, 'dubai ': 1, 'torrance, ca': 2, 'too many to name': 1, 'ky & southern california': 2, 'canada': 2, 'wien, österreich': 1, 'san pedro garza garcía, mexico': 1, 'rio de janeiro 🇧🇷': 1, 'planet earth': 1, 'constantinople': 1, 'uk': 3, 'jose ignacio-maldonado': 1, '⭐iii⭐we are everywhere⭐iii⭐': 1, 'brisbane, queensland': 1, 'the universe ': 1, 'olduğum yerdeyim': 1, 'jatland(gurugram)/losangeles': 1, 'tartarus\n\n': 1, 'estocolmo': 1, 'helgumsbro': 1, 'santiago de chile': 1, 'san francisco': 1, 'scottsdale, az': 1, 'follow/rt ≠ endorsement': 1, 'sweden': 1, 'delhi-ncr': 2, 'santa rita guam': 1, 'jakarta base': 1, 'poland': 1, 'vaduz': 2, 'bharuch, india': 1, 'jamshedpur, india': 2, 'selangor, malaysia': 1, 'internet': 3, '🌍    ': 1, 'beji, indonesia': 1, 'kind of somewhere nw of.': 1, '马德里, españa': 2, 'cleveland, ohio': 1, '澳洲': 1, 'são paulo, brasil': 1, 'united states of america': 1, 'u.k.': 1, 'cooper centre, kaptagat rd': 1, 'cleveland, oh': 1, 'stockholm, sweden': 1, 'bronxville': 1, 'austin, tx': 2, 'new york, usa 美国纽约': 2, 'exclusion zone - montserrat': 1, 'india. (bharat)': 1, 'ca': 1, 'buenos aires, argentina': 2, 'rio de janeiro': 1, '香港': 1, '地獄の地下深い穴底の底\u3000元天上界の住民\u3000主に許されば天上界': 1, 'green planet': 1, 'northern hemisphere ': 1, 'san francisco bay': 1, 'kathmandu': 2, 'toronto': 1, 'mauritius': 1, 'nh': 1, 'czech republic': 1, 'balıkesir, türkiye': 1, 'dera ismail khan, pakistan': 1, 'bielefeld': 1, 'punjab, pakistan': 2, 'sun': 1, 'brissie, australia': 1, 'moscow, russia': 1, 'beijing is india': 1, 'den haag': 1, 'normandie, france': 1, 'melbourne australia': 1, 'perugia - umbria - italia': 1, 'bangalore, india': 1, 'méxico/norway': 1, 'new york, usa  & new delhi, in': 1, 'universe    宇宙  ': 1, 'it’s a line blue line on earth': 1, 'city of london, london': 1, 'los angeles, ca': 1, '田舎': 1, 'taipei city, taiwan': 1, 'fort wayne, in': 1, 'leavenworth, kansas usa 🇺🇸': 1, '🗽': 1, 'oregon, usa': 1, 'venezuela': 1, '9th dimension': 1, '🇺🇸usa🇺🇸': 1, 'republic of texas': 1, 'oakville, ontario': 1, 'piramal school of leadership': 1, 'caribbean': 1, 'indiana, usa': 1, 'the back of a fedex truck': 1, 'the land of the free!': 1, 'narcostate': 1, 'backwash of fenerio': 1, 'sahiwal, punjab, pakistan': 1, 'bharat': 1, "kea'au hawaii": 1, 'rio grande do sul - brasil': 1, 'san isidro (bue)': 1, 'london u.k': 1, '13.0827° n, 80.2707° e': 1, 'islamabad, pakistan': 3, 'dallas, tx': 1, 'multan, pakistan': 1, 'weltweit': 1, 'brussels, belgium': 1, 'bring the truth through a picture': 2, 'london, uk': 2, 'پاکستان': 1, 'word': 1, 'entre alomejor y casiseguro': 1, 'islamabad pakistan ': 1, 'porto alegre/rs - brasil': 1, 'utrecht, the netherlands': 1, 'st paul, mn': 1, 'reno, nv': 1, 'barcelona - spain': 1, 'paris & brittany - france': 1, 'flemish site': 1, 'quetzaltenango': 1, 'puerto rico, usa': 1, 'jaipur': 1, 'the globe': 1, 'queens, ny': 1, 'no': 1, 'ghaziabad , delhi': 1, 'denver, co': 1, 'cheshire, belfast, elsewhere': 1, 'trollers gill, yorkshire dales': 2, 'roanoke, va / gatlinburg, tn': 1, 'nyc': 1, 'french czech brazilian in usa': 1, 'nagaur, india': 2, 'pakistan ': 1, 'vihiga, kenya ': 1, 'پشاور, پاکستان': 1, 'gikambura, kenya': 1, 'england': 1, 'pune, india': 1, 'chatham maritime': 1, 'bahiri gaun - 17, kirtipur': 1, 'uttar pradesh, india': 1, 'pokhara, nepal. ': 1, 'peshawar': 1, 'ri native living in texas': 1, 'encinitas, ca': 1, 'north america': 1, 'ohio, usa': 1, 'hither, and yon': 1, 'hillaryvillage, ca': 1, 'pdx': 1, 'bobbili, india': 1, '🇦🇺🔗🇵🇰': 1, 'in the bathroom': 1, 'mars': 1, 'larkano, pakistan': 1, 'हैदराबाद, भारत': 1, 'washington, d.c.': 1, 'rio largo/al ne 🇧🇷 slamérica': 1, 'kerala, india': 1, 'toronto, ontario': 1, 'toulouse, france': 1, '41° 54\' 8.02" n 12° 27\' 29" e': 1, '595, budhwar peth, pune': 1, 'mahindra group, india': 1, 'trichy': 1, 'makati city, national capital ': 1, 'hull, england': 1, 'shangri-la': 1, 'champaign, il': 2, 'tiruchirapalli, india': 1, 'charleston, sc': 1, 'மலேசியா': 1, 'ankara, türkiye': 1, 'talagang': 1, 'asmara, eritrea': 1, '#ladakh china😛': 1, 'kent, uk': 1, 'kent, united kingdom': 1, 'west up': 1, 'ছায়াপথ': 1, 'new delhi - haryana ': 1, 'idar,gujarat ': 1, 'delhi/punjab/haryana/west u.p': 1, 'united kingdom': 1, 'sumerpur, india ': 2, ' india': 1, 'thoothukudi': 1, 'loni, ghaziabad': 1, 'tamil nadu, india': 1, 'palladam': 1, 'chandigarh, india ': 1, 'coimbatore, tamilnadu': 1, 'திருவாரூர்': 1, 'mannargudi, tamil nadu, india': 1, 'main acct: @write2fite': 1, 'prayagraj': 1, 'lucknow, india': 1, 'america': 1, 'calgary 🇨🇦': 1, 'london ontario, canada': 1}

Done

<img width="452" alt="image" src="https://github.com/HB9398/social_media_scraper/assets/48625540/f731137c-620f-43b7-a125-0943fc57f7f5">
