-- MySQL dump 10.13  Distrib 8.0.26, for Linux (x86_64)
--
-- Host: localhost    Database: shop
-- ------------------------------------------------------
-- Server version	8.0.26

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Dumping data for table `address`
--

LOCK TABLES `address` WRITE;
/*!40000 ALTER TABLE `address` DISABLE KEYS */;
INSERT INTO `address` VALUES (1,2,'Bojan','Zdelar',NULL,'Svetozara Miletica 4','','Sremska Mitrovica','Vojvodina','Srbija',22000,NULL,0),(2,2,'Jovan','Zdelar',NULL,'Milutina Markovica 10',NULL,'Novi Sad','Vojvodina','Srbija',21000,NULL,0);
/*!40000 ALTER TABLE `address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `cart`
--

LOCK TABLES `cart` WRITE;
/*!40000 ALTER TABLE `cart` DISABLE KEYS */;
INSERT INTO `cart` VALUES (2,'combat-xl-mass-gainer',1), (2,'creatine',2);
/*!40000 ALTER TABLE `cart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES ('essentials','Essentials'),('fitmiss','FitMiss'),('on-the-go','On-The-Go'),('pre-post','Pre / Post'),('protein','Protein'),('swag','Swag');
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (1,2,'bojan@zdelar.com',1,2,1,1,0,0);
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `payment_method`
--

LOCK TABLES `payment_method` WRITE;
/*!40000 ALTER TABLE `payment_method` DISABLE KEYS */;
INSERT INTO `payment_method` VALUES (1,'Credit card'),(2,'Pay at delivery');
/*!40000 ALTER TABLE `payment_method` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES ('assault-energy-strength','Assault Energy+Strength','ATHLETIC PERFORMANCE\nWITH AN EDGE.\n\nMusclePharm® Assault™ Energy+Strength is creating the new standard in performance pre-workouts. University studied and designed specifically for the modern-day athlete, Assault™ provides unmatched energy and boosts your performance during intensive. Assault™ features one of the most studied and scientifically proven supplements for strength gains in Creatine Monohydrate. Also featured is Carnosyn® Beta-Alanine that works to buffer lactic acid built up from strenuous exercise, reducing performance fatigue, and prolonging your intense workouts. All of this, plus an Explosive Energy & Focus blend to help you attack your training right out of the gate are what make Assault™ the next level of pre-workout nutrition.',26.99,10,'https://cdn.shopify.com/s/files/1/1618/2767/products/SportSeries_Assault_30Servings_BlueRasberry_view1_360x.jpg?v=1542060696','https://cdn.shopify.com/s/files/1/1618/2767/products/SportSeries_Assault_30Servings_FruitPunch_view1_1800x1800.jpg?v=1542060696',10,0),('assault-pre-workout','Assault Pre-Workout','Assault is MusclePharm\'s tried and true pre-workout. For just $19.99, you\'re getting a month\'s worth (30 servings) of fuel to power you past your prior performance limits. Great tasting, energy-enhancing, and tested to be banned substance free.\n\nHere\'s what you\'re getting:\n\n    200mg of caffeine (for energy and focus)\n    150 mg of Acetyl-L-Carnitine (for energy and focus)\n    500mg of Taurine (muscle fuel)\n    500 mg of L-Glycine (more muscle fuel)\n    1.5g of creatine monohydrate (for strength and performance)\n    1.6g of CarnoSyn Beta-Alanine (for strength and performance)\n    500 mg of Betaine Anhydrous (for strength and performance)\n    Vitamin C (300mg), E (40IU), B6 (20mg) and B12 (50mcg)\n\nHere\'s what you\'re not getting:\n\n    No carbs\n    No calories\n    No sugars\n',19.99,10,'https://cdn.shopify.com/s/files/1/1618/2767/products/SportSeries_AssaultFDM_30Serve_FruitPunch_360x.jpg?v=1594761101','https://cdn.shopify.com/s/files/1/1618/2767/products/SportSeries_AssaultFDM_30Serve_FruitPunch_1800x1800.jpg?v=1594761101',5,0),('bcaa','BCAA','DEMAND MORE OF YOUR BODY AND YOUR BCAA.\n\nMusclePharm® BCAA offers a unique patent-pending ratio—3 Leucine, 1 Isoleucine, 2 Valine—that is specifically tuned to deliver the ideal amounts of these three amino acids during all phases of muscle development and maintenance. Through this formulation, amino acids are released both before and after a workout. MP® BCAA minimizes muscle damage, while supporting increased lean body mass.\n\n \n\nProduct Benefits:\n\n    Supports Lean Mass Growth\n    Reduces Muscle Breakdown\n    Increases Protein Synthesis\n',14.99,10,'https://cdn.shopify.com/s/files/1/1618/2767/products/Essentials_BCAA_3serve_BlueRasberry_360x.jpg?v=1550095695','https://cdn.shopify.com/s/files/1/1618/2767/products/Essentials_BCAA_30serve_caps_1800x1800.jpg?v=1542062133',0,0),('bcaa-capsules','BCAA Capsules','DEMAND MORE OF YOUR\nBODY AND YOUR BCAA.\n\nMusclePharm® BCAA offers a unique patent-pending ratio—3 Leucine, 1 Isoleucine, 2 Valine—that is specifically tuned to deliver the ideal amounts of these three amino acids during all phases of muscle development and maintenance. Through this formulation, amino acids are released both before and after a workout. MP® BCAA minimizes muscle damage, while supporting increased lean body mass.\n\n \n\nProduct Benefits:\n\n    Supports Lean Mass Growth\n    Reduces Muscle Breakdown\n    Increases Protein Synthesis\n\n    These statements have not been evaluated by the Food and Drug Administration. This product is not intended to diagnose, treat, cure or prevent any disease. \n',14.99,10,'https://cdn.shopify.com/s/files/1/1618/2767/products/Essentials_BCAA_30serve_caps_360x.jpg?v=1542062133','https://cdn.shopify.com/s/files/1/1618/2767/products/Essentials_BCAA_30serve_caps_1800x1800.jpg?v=1542062133',0,0),('combat-100-whey','Combat 100% Whey','Ultra-Premium 100% Whey Protein\n\nCombat 100% Whey™ is an ultra-premium blend containing 100% whey protein. It is for athletes looking to maintain lean muscle and replenish nutrients after workouts to fuel muscle recovery and performance that tastes great and mixes easily.\nGet More Out Of Every Scoop\n\nEvery scoop of Combat 100% Whey™ is packed with 25g of 100% whey protein as whey protein isolate and whey protein concentrate that digests quickly to help satisfy your daily protein needs. In addition, Combat 100% Whey™ is low in fats and free of artificial dyes, fillers, gluten, and other undesirable ingredients. Take any time of day, before or after a workout, to fuel the athlete inside of you with an ultra-premium, quality protein experience.\nQuality at Its Finest\n\nEvery single batch of Combat 100% Whey™ is tested for both banned substances and protein label claim verification. We have over 20 million products certified with globally-recognized Informed-Choice to date. At MusclePharm®, we go the extra distance to ensure our customers get exactly what they expect. We test all batches for banned substances, as well as protein quality, to verify that we consistently deliver 25g of protein. That is why millions of customers trust MusclePharm®. #WeLiveThis #MPNation',28.99,10,'https://cdn.shopify.com/s/files/1/1618/2767/products/SportSeries_Combat100Whey_2lb_ChocolateMilk_view1_360x.jpg?v=1559580599','https://cdn.shopify.com/s/files/1/1618/2767/products/SportSeries_Combat100Whey_5lb_Strawberry_view1_1800x1800.jpg?v=1559580599',0,0),('combat-crunch-protein-bars','Combat Crunch Protein Bars','FUELING SPORT WITH A MULTI-LAYER BAKED PROTEIN BAR!\n\nCombat Crunch™ baked protein bars are made using a proprietary baking process for superior taste and a softer texture. The bars are high protein, with low active carbs and tons of fiber. Unlike hard-paste, “taffy-like” sports bars, Combat Crunch™ is like eating a soft-batch cookie.',24.99,10,'https://cdn.shopify.com/s/files/1/1618/2767/products/SportSeries_CombatCrunch_12serve_ChocolateCake_360x.jpg?v=1594413685','https://cdn.shopify.com/s/files/1/1618/2767/products/SportSeries_CombatCrunch_12serve_CookieDough_view1_1800x1800.jpg?v=1594413685',2,0),('combat-protein','Combat Protein','Fuels Muscles & Performance for hours!\nThis is 25 Grams of High-Quality Protein in a Tasty, Easy-To-Mix Shake, Formulated for Athletes and Active People.\n\nPeople who train hard demand a superior and more effective protein. To maximize lean muscle growth and recovery ensuring proper protein utilization, MusclePharm® scientists fortified Combat Protein Powder® with a variety of protein blends that digest at varying rates—this helps fuel your muscles longer. The great-tasting, easy-mixing digestive blend is fine-tuned for true nutrient utilization–a step ahead in protein powder technology. Most other protein products seem to be okay with the status quo, the minimum. But ask yourself: do you give your workouts minimum effort? MusclePharm® scientists over-delivered. Combat Protein Powder® is precision-engineered with whey protein concentrates, hydrolysates and isolates, egg albumin, and micellar casein. These help create a muscle-building environment for longer periods of time, which results in greater muscle building, recovery and performance.',26.99,10,'https://cdn.shopify.com/s/files/1/1618/2767/products/SportSeries_CombatProtein_2lb_ChocolatePeanutButter_view1_360x.jpg?v=1559580836','https://cdn.shopify.com/s/files/1/1618/2767/products/SportSeries_CombatProtein_2lb_ChocolateMilk_view1_1800x1800.jpg?v=1559580836',5,0),('combat-xl-mass-gainer','Combat XL Mass Gainer','MusclePharm® Combat XL™ is a revolutionary weight gaining supplement formulated with dense, functional calories and essential nutrients partitioned precisely to create the perfect muscle building environment an athlete needs. Featuring essential fatty acids, complex carbohydrates, and 4 sources of protein, Combat XL works to promote muscle recovery allowing you to get big – and stay big!\n\nProduct benefits \n\n    1270 Calories\n    50 grams of muscle building protein\n    252 grams of carbohydrates\n    MCTS, Flax,and Chia Seeds\n',28.99,10,'https://cdn.shopify.com/s/files/1/1618/2767/products/SportSeries_CombatXLMassGainer_6lb_ChocolateMilk_view1_360x.jpg?v=1559162878','https://cdn.shopify.com/s/files/1/1618/2767/products/SportSeries_CombatXLMassGainer_6lb_Vanilla_view1_1800x1800.jpg?v=1559162878',1,0),('creatine','Creatine','ELEVATE YOUR PERFORMANCE!\n\nOne of the most clinically researched compounds available, MusclePharm®  Creatine Monohydrate works to restore muscular energy levels depleted during exercise, resulting in increased strength, power, muscular endurance, and lean body mass. MusclePharm® Creatine features 5 grams of Creatine Monohydrate per serving, delivering a maximal impact on athletic performance with every use.\n\n \n\nProduct Benefits:\n\n    Strength and Power Amplifier\n    Improves Athletic Performance\n    Promotes increases in strength and lean body mass\n\n    These statements have not been evaluated by the Food and Drug Administration. This product is not intended to diagnose, treat, cure or prevent any disease. \n',9.99,10,'https://cdn.shopify.com/s/files/1/1618/2767/products/Essentials_Creatine_60serve_360x.jpg?v=1542066901','https://cdn.shopify.com/s/files/1/1618/2767/products/Essentials_Creatine_60serve_1800x1800.jpg?v=1542066901',15,0),('fish-oil','Fish Oil','SUPPLEMENTATION THE\nWAY NATURE INTENDED.\n\n MusclePharm® Fish Oil is tuned for those of us who hit the gym. Essential Fatty Acids, or EFAs, are essential to the human body but can only be found in a few species of fish. Athletes supplement their diets with fish oil because research suggests fish oil’s fatty acids can assist with heart function, carbohydrate breakdown and joint health.\n\n \n\nProduct benefits:\n\n    High Quality EPA/DHA\n    Supports Heart, Brain, and Joint Function\n    1,000 MG of Fish Oil\n    Natural Citrus Flavor\n\n    These statements have not been evaluated by the Food and Drug Administration. This product is not intended to diagnose, treat, cure or prevent any disease. \n\n',13.99,10,'https://cdn.shopify.com/s/files/1/1618/2767/products/Essentials_FishOil_90serve_caps_360x.jpg?v=1542067041','https://cdn.shopify.com/s/files/1/1618/2767/products/Essentials_FishOil_90serve_caps_1800x1800.jpg?v=1542067041',0,0),('fitmiss-delight','FitMiss Delight','EAT LESS. FEEL FULLER. LOSE WEIGHT.\n\nFinally. A nutrition shake for women that satisfies hunger while providing real results. FitMiss Delight® utilizes the vegetable-based protein weight-loss sensation SolaThin®, which helps you feel full faster. Along with this fast-acting protein, FitMiss Delight® also delivers a full day’s essential nutrients with quality calories. The unique blend of fruits and vegetables delivers optimal levels of digestive enzymes, vitamins and minerals. The gluten-free balance of carbohydrates, fats, and high-quality proteins provide sustained energy and appetite satisfaction. FitMiss Delight® is the complete choice, real natural goodness. Drink it every day—you’ll feel more satisfied and lose weight! This combination of healthy ingredients works together, synergistically, to provide nutritional support for lean muscle tissue, fat loss and increased energy.',19.99,10,'https://cdn.shopify.com/s/files/1/1618/2767/products/Fitmiss_Delight_1.2lb_VanillaChai_360x.jpg?v=1559323489','https://cdn.shopify.com/s/files/1/1618/2767/products/FM_Delight_2lb_Chocolate_1800x1800.jpg?v=1559323489',0,0),('glutamine','Glutamine','DEMAND MORE OF YOUR BODY AND YOUR GLUTAMINE\n\nMusclePharm®\'s Glutamine increases whole body glutamine status by enhancing uptake, bioavailability and digestion. This ultimately provides optimal muscle-tissue saturation through a substantial 5 gram serving of L-Glutamine that delivers a wide range of benefits. MusclePharm®\'s Glutamine helps you rehydrate, rebuild and recover faster and more efficiently from even the toughest of workouts.\n\n    These statements have not been evaluated by the Food and Drug Administration. This product is not intended to diagnose, treat, cure or prevent any disease.',14.99,10,'https://cdn.shopify.com/s/files/1/1618/2767/products/Essentials_Glutamine_60serve_Unflavored_360x.jpg?v=1542067148','https://cdn.shopify.com/s/files/1/1618/2767/products/Essentials_Glutamine_60serve_Unflavored_1800x1800.jpg?v=1542067148',0,0),('mp-duffle-bag','MP Duffle Bag','Rep \'We Live This\' in style with this limited edition MusclePharm dufflebag!\n\n    Measuring 28 inches long by 11 inches wide and 11 inches high, you can store plenty of your gym gear in this bag, or use it to store other stuff\n    Three exterior pockets and several interior pouches keep things organized\n    The MP logo on the side and on the zipper pulls reps your MP pride while keeping it classy',45,10,'https://cdn.shopify.com/s/files/1/1618/2767/products/NRB_6407_360x.jpg?v=1598641105','https://cdn.shopify.com/s/files/1/1618/2767/products/NRB_6419_jpg_1800x1800.png?v=1598641105',0,0),('mp-logo-t-shirt','MP Logo T-Shirt','Simple, soft, majestic. Rep your MP pride with this classy tee. Suitable for the gym or on-the-go, you\'ve got your MP logo on the front and clean shoulders and back. Available as a limited run in Small, Medium, Large and Extra Large.',15,10,'https://cdn.shopify.com/s/files/1/1618/2767/products/NRB_6434_360x.jpg?v=1599154603','https://cdn.shopify.com/s/files/1/1618/2767/products/NRB_6434_1800x1800.jpg?v=1599154603',0,0),('multi-v-multivitamin','Multi-V+ Multivitamin','A SERIOUSLY ENHANCED MULTI-VITAMIN.\n\nMusclePharm® Multi-V+ is the perfect multi-vitamin designed for athletes at every level. Packed with high-potency vitamins and minerals, this multi plays a critical role in replenishing your body. MusclePharm® Multi-V+ is here to support your goals.\n\n \n\nKey Features:\n\n    Immune Support with 20+ Ingredients\n    Helps Support Joint Function\n    Antioxidants\n',14.99,10,'https://cdn.shopify.com/s/files/1/1618/2767/products/Essentials_MultiV_30serve_caps_360x.jpg?v=1542067234','https://cdn.shopify.com/s/files/1/1618/2767/products/Essentials_MultiV_30serve_caps_1800x1800.jpg?v=1542067234',0,0),('musclepharm-backpack','MusclePharm Backpack','Get one while they last! We have just 35 MusclePharm branded backpacks suitable for your workout gear, school, work, the car, or other light activity. The backpack is embroidered with the MP logo and MP branded zipper pulls on each of the four zippered compartments. These won\'t last long and is not available in stores, so snag one while you can!\n\nKey Details:\n\n    Lightweight backpack with four zippered pouches\n    Backpack measures about 17 inches tall by 13 inches wide\n    Embroidered MP logo on face and MP branded zipper pulls\n    Padded and vented surfaces on the back and under the shoulder straps\n    Not returnable once used\n',35,10,'https://cdn.shopify.com/s/files/1/1618/2767/products/NRB_6411_resize_360x.jpg?v=1597788640','https://cdn.shopify.com/s/files/1/1618/2767/products/NRB_6411_resize_1800x1800.jpg?v=1597788640',0,0),('musclepharm-black-green-shaker-bottle','MusclePharm Black & Green Shaker Bottle','MusclePharm Shaker Bottle- 25 oz. Blend your powdered supplements perfectly with the MusclePharm shaker bottle. Ideal for taking your supplements on the go, this easy to use bottle ensures you are never without your supplements. You no longer have to worry about powdery clumps or leaky containers, this shaker has you covered!\n\n \n\nKey Features:\n\n    Secure, leak proof lid\n    Removable strainer\n    Precise measurement markings\n    BPA Free\n    Dishwasher Safe\n    Bold “MP” and “We Live This” logos\n',9,10,'https://cdn.shopify.com/s/files/1/1618/2767/products/Shaker_Bottle_-_Sport_Series_grande_9fb20d68-4075-43b5-8b21-9afaa71ca23f_360x.png?v=1542301789','https://cdn.shopify.com/s/files/1/1618/2767/products/Shaker_Bottle_-_Sport_Series_grande_9fb20d68-4075-43b5-8b21-9afaa71ca23f_1800x1800.png?v=1542301789',0,0),('musclepharm-mass-gainer','MusclePharm Mass Gainer','MusclePharm® Mass Gainer is a revolutionary weight gaining supplement formulated with dense, functional calories and essential nutrients partitioned precisely to create the perfect muscle building environment an athlete needs. Featuring complex carbohydrates and three sources of protein, MusclePharm® Mass Gainer works to promote muscle recovery allowing you to get big – and stay big!\n\nKey Features \n\n    1200+ Calories\n    50G OF MUSCLE BUILDING PROTEIN\n    BANNED SUBSTANCE TESTED\n    NO ARTIFICIAL DYES OR COLORS\n',24.99,10,'https://cdn.shopify.com/s/files/1/1618/2767/products/StealthSeries_MassGainer_3lb_Chocolate_1ebd47d6-1b9e-4bb4-9222-ab4901189b7b_360x.jpg?v=1542301638','https://cdn.shopify.com/s/files/1/1618/2767/products/StealthSeries_MassGainer_3lb_Chocolate_1ebd47d6-1b9e-4bb4-9222-ab4901189b7b_1800x1800.jpg?v=1542301638',0,0),('shred-sport-fat-burner','Shred Sport Fat Burner','MusclePharm Shred Sport is the next generation of weight loss and energy that utilizes safe, effective, and researched ingredients to burn fat, provide intense energy and remarkable results. This fast-acting fat burner targets stored body fat, controls appetite and supports your metabolism. No inferior herbal blends here, just powerful ingredients proven to bring you closer to your performance goals!\n\n    These statements have not been evaluated by the Food and Drug Administration. This product is not intended to diagnose, treat, cure or prevent any disease. ',29.99,10,'https://cdn.shopify.com/s/files/1/1618/2767/products/SportSeries_ShredSport_30Serve_360x.jpg?v=1594839452','https://cdn.shopify.com/s/files/1/1618/2767/products/SportSeries_ShredSport_30Serve_1800x1800.jpg?v=1594839452',0,0),('stealth-series-100-whey','Stealth Series 100% Whey','MusclePharm® 100% WHEY is an ultra-premium formula containing 100% whey protein.* It is for athletes looking to maintain lean muscle and replenish nutrients after workouts to fuel muscle recovery. Performance that tastes great and mixes easily! MusclePharm® 100% WHEY is tested for both banned substances and protein label claim verification. We have over 20 million products certified with globally recognized Informed-Choice to date. At MusclePharm®, we go the extra distance to ensure our customers get exactly what they expect.\n\n \n\nKey Features:\n\n    25 G OF 100% WHEY PROTEIN\n    AMAZING TASTE & EASY TO MIX\n    BANNED SUBSTANCE TESTED\n    NO ARTIFICIAL DYES OR COLORS\n',29.99,10,'https://cdn.shopify.com/s/files/1/1618/2767/products/StealthSeries_100Whey_2lb_Chocolate_2c3237fc-f42c-4640-a527-4cbb6f5c5be4_360x.jpg?v=1542070940','https://cdn.shopify.com/s/files/1/1618/2767/products/StealthSeries_100Whey_2lb_Vanilla_5f1b1296-849b-4ce7-be0b-ffe437a2c633_1800x1800.jpg?v=1542070940',0,0),('z-pm-sleep-aid','Z-PM Sleep Aid','Demand more of your body.\n\nMusclePharm® Z-PM Essentials™ promotes deeper and more efficient sleep to maximize healing, tissue repair, anabolic hormone production, testosterone levels and muscle growth. It delivers the benefits of precise dosages and Z-Core PM™ ingredient ratios, and adds the synergistic effects of fenugreek to support natural levels of free testosterone and healthy libido function in women and men.\n\n \n\nProduct benefits:\n\n    Supports Natural Testosterone\n    Promotes Deep Sleep & Recovery\n    Supports Healthy Libido Function\n    60 Servings\n\n    These statements have not been evaluated by the Food and Drug Administration. This product is not intended to diagnose, treat, cure or prevent any disease. \n',14.99,10,'https://cdn.shopify.com/s/files/1/1618/2767/products/Essentials_ZPM_60serve_caps_360x.jpg?v=1542067451','https://cdn.shopify.com/s/files/1/1618/2767/products/Essentials_ZPM_60serve_caps_1800x1800.jpg?v=1542067451',0,0);
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `product_in_category`
--

LOCK TABLES `product_in_category` WRITE;
/*!40000 ALTER TABLE `product_in_category` DISABLE KEYS */;
INSERT INTO `product_in_category` VALUES ('bcaa','essentials'),('bcaa-capsules','essentials'),('creatine','essentials'),('fish-oil','essentials'),('glutamine','essentials'),('multi-v-multivitamin','essentials'),('z-pm-sleep-aid','essentials'),('fitmiss-delight','fitmiss'),('musclepharm-backpack','on-the-go'),('assault-energy-strength','pre-post'),('assault-pre-workout','pre-post'),('shred-sport-fat-burner','pre-post'),('combat-100-whey','protein'),('combat-crunch-protein-bars','protein'),('combat-protein','protein'),('combat-xl-mass-gainer','protein'),('fitmiss-delight','protein'),('musclepharm-mass-gainer','protein'),('stealth-series-100-whey','protein'),('mp-duffle-bag','swag'),('mp-logo-t-shirt','swag'),('musclepharm-backpack','swag'),('musclepharm-black-green-shaker-bottle','swag');
/*!40000 ALTER TABLE `product_in_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `product_in_order`
--

LOCK TABLES `product_in_order` WRITE;
/*!40000 ALTER TABLE `product_in_order` DISABLE KEYS */;
INSERT INTO `product_in_order` VALUES ('assault-energy-strength',1,2),('combat-protein',1,1);
/*!40000 ALTER TABLE `product_in_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `shipping_method`
--

LOCK TABLES `shipping_method` WRITE;
/*!40000 ALTER TABLE `shipping_method` DISABLE KEYS */;
INSERT INTO `shipping_method` VALUES (1,'Free Shipping',0),(2,'Standard Shipping & Handling',9.99),(3,'Expedited Shipping & Handling',16.99);
/*!40000 ALTER TABLE `shipping_method` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'admin@musclepharm.com','sha256$0G5OnI4f$2a52e84181d5496da2567637a7e06d5c706e8b54b2d88d161c9e0c3c62586380','Bojan','Zdelar',1),(2,'bojan@zdelar.com','sha256$EudqGDA9$d069e473e0f605da41df8a91c7679c323f6d66675a084261f92c7e190f356633','Bojan','Zdelar',2),(3,'marija@dostanic.com','sha256$fx1cOqPN$fcd5ab7cf4668f17f326b1d838292a030560f80b0a328797ef5efc107698061d','Marija','Dostanic',2);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `user_type`
--

LOCK TABLES `user_type` WRITE;
/*!40000 ALTER TABLE `user_type` DISABLE KEYS */;
INSERT INTO `user_type` VALUES (1,'admin'),(2,'buyer');
/*!40000 ALTER TABLE `user_type` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-10-05 20:22:02
