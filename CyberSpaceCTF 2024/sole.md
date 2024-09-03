- Given an ELF64 file

![image](https://github.com/user-attachments/assets/b14b7652-54f2-4f57-a698-b3db7f0ad485)

- IDA's pseudocode ( I've renamed some functions/variables and cropped unrelated code snippets for easier analysis)
```C
 flag_0 = *(_DWORD *)_$LT$alloc..vec..Vec$LT$T$C$A$GT$$u20$as$u20$core..ops..index..Index$LT$I$GT$$GT$::index::hd11ab854543a4636(
                        (int)v364,
                        0,
                        (int)&off_55A38,
                        v9,
                        v10,
                        v11,
                        v93,
                        v120,
                        v148,
                        v175,
                        v202,
                        v229,
                        v256,
                        v283);
  flag_1 = *(_DWORD *)_$LT$alloc..vec..Vec$LT$T$C$A$GT$$u20$as$u20$core..ops..index..Index$LT$I$GT$$GT$::index::hd11ab854543a4636(
                        (int)v364,
                        1,
                        (int)&off_55A50,
                        v12,
                        v13,
                        v14,
                        v94,
                        v121,
                        v149,
                        v176,
                        v203,
                        v230,
                        v257,
                        v284);
  flag_2 = *(_DWORD *)_$LT$alloc..vec..Vec$LT$T$C$A$GT$$u20$as$u20$core..ops..index..Index$LT$I$GT$$GT$::index::hd11ab854543a4636(
                        (int)v364,
                        2,
                        (int)&off_55A68,
                        v15,
                        v16,
                        v17,
                        v95,
                        v122,
                        v150,
                        v177,
                        v204,
                        v231,
                        v258,
                        v285);
  flag_3 = *(_DWORD *)_$LT$alloc..vec..Vec$LT$T$C$A$GT$$u20$as$u20$core..ops..index..Index$LT$I$GT$$GT$::index::hd11ab854543a4636(
                        (int)v364,
                        3,
                        (int)&off_55A80,
                        v18,
                        v19,
                        v20,
                        v96,
                        v123,
                        v151,
                        v178,
                        v205,
                        v232,
                        v259,
                        v286);
  flag_4 = *(_DWORD *)_$LT$alloc..vec..Vec$LT$T$C$A$GT$$u20$as$u20$core..ops..index..Index$LT$I$GT$$GT$::index::hd11ab854543a4636(
                        (int)v364,
                        4,
                        (int)&off_55A98,
                        v21,
                        v22,
                        v23,
                        v97,
                        v124,
                        v152,
                        v179,
                        v206,
                        v233,
                        v260,
                        v287);
  flag_5 = *(_DWORD *)_$LT$alloc..vec..Vec$LT$T$C$A$GT$$u20$as$u20$core..ops..index..Index$LT$I$GT$$GT$::index::hd11ab854543a4636(
                        (int)v364,
                        5,
                        (int)&off_55AB0,
                        v24,
                        v25,
                        v26,
                        v98,
                        v125,
                        v153,
                        v180,
                        v207,
                        v234,
                        v261,
                        v288);
  flag_6 = *(_DWORD *)_$LT$alloc..vec..Vec$LT$T$C$A$GT$$u20$as$u20$core..ops..index..Index$LT$I$GT$$GT$::index::hd11ab854543a4636(
                        (int)v364,
                        6,
                        (int)&off_55AC8,
                        v27,
                        v28,
                        v29,
                        v99,
                        v126,
                        v154,
                        v181,
                        v208,
                        v235,
                        v262,
                        v289);
  flag_7 = *(_DWORD *)_$LT$alloc..vec..Vec$LT$T$C$A$GT$$u20$as$u20$core..ops..index..Index$LT$I$GT$$GT$::index::hd11ab854543a4636(
                        (int)v364,
                        7,
                        (int)&off_55AE0,
                        v30,
                        v31,
                        v32,
                        v100,
                        v127,
                        v155,
                        v182,
                        v209,
                        v236,
                        v263,
                        v290);
  flag_8 = *(_DWORD *)_$LT$alloc..vec..Vec$LT$T$C$A$GT$$u20$as$u20$core..ops..index..Index$LT$I$GT$$GT$::index::hd11ab854543a4636(
                        (int)v364,
                        8,
                        (int)&off_55AF8,
                        v33,
                        v34,
                        v35,
                        v101,
                        v128,
                        v156,
                        v183,
                        v210,
                        v237,
                        v264,
                        v291);
  flag_9 = *(_DWORD *)_$LT$alloc..vec..Vec$LT$T$C$A$GT$$u20$as$u20$core..ops..index..Index$LT$I$GT$$GT$::index::hd11ab854543a4636(
                        (int)v364,
                        9,
                        (int)&off_55B10,
                        v36,
                        v37,
                        v38,
                        v102,
                        v129,
                        v157,
                        v184,
                        v211,
                        v238,
                        v265,
                        v292);
  flag_10 = *(_DWORD *)_$LT$alloc..vec..Vec$LT$T$C$A$GT$$u20$as$u20$core..ops..index..Index$LT$I$GT$$GT$::index::hd11ab854543a4636(
                         (int)v364,
                         10,
                         (int)&off_55B28,
                         v39,
                         v40,
                         v41,
                         v103,
                         v130,
                         v158,
                         v185,
                         v212,
                         v239,
                         v266,
                         v293);
  flag_11 = *(_DWORD *)_$LT$alloc..vec..Vec$LT$T$C$A$GT$$u20$as$u20$core..ops..index..Index$LT$I$GT$$GT$::index::hd11ab854543a4636(
                         (int)v364,
                         11,
                         (int)&off_55B40,
                         v42,
                         v43,
                         v44,
                         v104,
                         v131,
                         v159,
                         v186,
                         v213,
                         v240,
                         v267,
                         v294);
  flag_12 = *(_DWORD *)_$LT$alloc..vec..Vec$LT$T$C$A$GT$$u20$as$u20$core..ops..index..Index$LT$I$GT$$GT$::index::hd11ab854543a4636(
                         (int)v364,
                         12,
                         (int)&off_55B58,
                         v45,
                         v46,
                         v47,
                         v105,
                         v132,
                         v160,
                         v187,
                         v214,
                         v241,
                         v268,
                         v295);
  flag_13 = *(_DWORD *)_$LT$alloc..vec..Vec$LT$T$C$A$GT$$u20$as$u20$core..ops..index..Index$LT$I$GT$$GT$::index::hd11ab854543a4636(
                         (int)v364,
                         13,
                         (int)&off_55B70,
                         v48,
                         v49,
                         v50,
                         v106,
                         v133,
                         v161,
                         v188,
                         v215,
                         v242,
                         v269,
                         v296);
  flag_14 = *(_DWORD *)_$LT$alloc..vec..Vec$LT$T$C$A$GT$$u20$as$u20$core..ops..index..Index$LT$I$GT$$GT$::index::hd11ab854543a4636(
                         (int)v364,
                         14,
                         (int)&off_55B88,
                         v51,
                         v52,
                         v53,
                         v107,
                         v134,
                         v162,
                         v189,
                         v216,
                         v243,
                         v270,
                         v297);
  flag_15 = *(_DWORD *)_$LT$alloc..vec..Vec$LT$T$C$A$GT$$u20$as$u20$core..ops..index..Index$LT$I$GT$$GT$::index::hd11ab854543a4636(
                         (int)v364,
                         15,
                         (int)&off_55BA0,
                         v54,
                         v55,
                         v56,
                         v108,
                         v135,
                         v163,
                         v190,
                         v217,
                         v244,
                         v271,
                         v298);
  flag_16 = *(_DWORD *)_$LT$alloc..vec..Vec$LT$T$C$A$GT$$u20$as$u20$core..ops..index..Index$LT$I$GT$$GT$::index::hd11ab854543a4636(
                         (int)v364,
                         16,
                         (int)&off_55BB8,
                         v57,
                         v58,
                         v59,
                         v109,
                         v136,
                         v164,
                         v191,
                         v218,
                         v245,
                         v272,
                         v299);
  flag_17 = *(_DWORD *)_$LT$alloc..vec..Vec$LT$T$C$A$GT$$u20$as$u20$core..ops..index..Index$LT$I$GT$$GT$::index::hd11ab854543a4636(
                         (int)v364,
                         17,
                         (int)&off_55BD0,
                         v60,
                         v61,
                         v62,
                         v110,
                         v137,
                         v165,
                         v192,
                         v219,
                         v246,
                         v273,
                         v300);
  flag_18 = *(_DWORD *)_$LT$alloc..vec..Vec$LT$T$C$A$GT$$u20$as$u20$core..ops..index..Index$LT$I$GT$$GT$::index::hd11ab854543a4636(
                         (int)v364,
                         18,
                         (int)&off_55BE8,
                         v63,
                         v64,
                         v65,
                         v111,
                         v138,
                         v166,
                         v193,
                         v220,
                         v247,
                         v274,
                         v301);
  flag_19 = *(_DWORD *)_$LT$alloc..vec..Vec$LT$T$C$A$GT$$u20$as$u20$core..ops..index..Index$LT$I$GT$$GT$::index::hd11ab854543a4636(
                         (int)v364,
                         19,
                         (int)&off_55C00,
                         v66,
                         v67,
                         v68,
                         v112,
                         v139,
                         v167,
                         v194,
                         v221,
                         v248,
                         v275,
                         v302);
  flag_20 = *(_DWORD *)_$LT$alloc..vec..Vec$LT$T$C$A$GT$$u20$as$u20$core..ops..index..Index$LT$I$GT$$GT$::index::hd11ab854543a4636(
                         (int)v364,
                         20,
                         (int)&off_55C18,
                         v69,
                         v70,
                         v71,
                         v113,
                         v140,
                         v168,
                         v195,
                         v222,
                         v249,
                         v276,
                         v303);
  flag_21 = *(_DWORD *)_$LT$alloc..vec..Vec$LT$T$C$A$GT$$u20$as$u20$core..ops..index..Index$LT$I$GT$$GT$::index::hd11ab854543a4636(
                         (int)v364,
                         21,
                         (int)&off_55C30,
                         v72,
                         v73,
                         v74,
                         v114,
                         v141,
                         v169,
                         v196,
                         v223,
                         v250,
                         v277,
                         v304);
  flag_22 = *(_DWORD *)_$LT$alloc..vec..Vec$LT$T$C$A$GT$$u20$as$u20$core..ops..index..Index$LT$I$GT$$GT$::index::hd11ab854543a4636(
                         (int)v364,
                         22,
                         (int)&off_55C48,
                         v75,
                         v76,
                         v77,
                         v115,
                         v142,
                         v170,
                         v197,
                         v224,
                         v251,
                         v278,
                         v305);
  flag_23 = *(_DWORD *)_$LT$alloc..vec..Vec$LT$T$C$A$GT$$u20$as$u20$core..ops..index..Index$LT$I$GT$$GT$::index::hd11ab854543a4636(
                         (int)v364,
                         23,
                         (int)&off_55C60,
                         v78,
                         v79,
                         v80,
                         v116,
                         v143,
                         v171,
                         v198,
                         v225,
                         v252,
                         v279,
                         v306);
  flag_24 = *(_DWORD *)_$LT$alloc..vec..Vec$LT$T$C$A$GT$$u20$as$u20$core..ops..index..Index$LT$I$GT$$GT$::index::hd11ab854543a4636(
                         (int)v364,
                         24,
                         (int)&off_55C78,
                         v81,
                         v82,
                         v83,
                         v117,
                         v144,
                         v172,
                         v199,
                         v226,
                         v253,
                         v280,
                         v307);
  flag_25 = *(_DWORD *)_$LT$alloc..vec..Vec$LT$T$C$A$GT$$u20$as$u20$core..ops..index..Index$LT$I$GT$$GT$::index::hd11ab854543a4636(
                         (int)v364,
                         25,
                         (int)&off_55C90,
                         v84,
                         v85,
                         v86,
                         v118,
                         v145,
                         v173,
                         v200,
                         v227,
                         v254,
                         v281,
                         v308);
  v332 = flag_19 * flag_11;
  if ( !is_mul_ok(flag_19, flag_11) )
    core::panicking::panic::h8705e81f284be8a5();
  if ( !is_mul_ok(flag_4, v332) )
    core::panicking::panic::h8705e81f284be8a5();
  if ( flag_4 * v332 != 391020 )
    v363 = 1;
  v330 = flag_13 * flag_8;
  if ( !is_mul_ok(flag_13, flag_8) )
    core::panicking::panic::h8705e81f284be8a5();
  if ( !is_mul_ok(flag_22, v330) )
    core::panicking::panic::h8705e81f284be8a5();
  if ( flag_22 * v330 != 567720 )
    v363 = 1;
  v329 = flag_22 * flag_0;
  if ( !is_mul_ok(flag_22, flag_0) )
    core::panicking::panic::h8705e81f284be8a5();
  if ( __OFADD__(flag_15, v329) )
    core::panicking::panic::h8705e81f284be8a5();
  if ( flag_15 + v329 != 4872 )
    v363 = 1;
  v328 = flag_0 + flag_8;
  if ( __OFADD__(flag_0, flag_8) )
    core::panicking::panic::h8705e81f284be8a5();
  if ( __OFADD__(flag_11, v328) )
    core::panicking::panic::h8705e81f284be8a5();
  if ( flag_11 + v328 != 199 )
    v363 = 1;
  v327 = flag_22 * flag_12;
  if ( !is_mul_ok(flag_22, flag_12) )
    core::panicking::panic::h8705e81f284be8a5();
  if ( __OFSUB__(flag_13, v327) )
    core::panicking::panic::h8705e81f284be8a5();
  if ( flag_13 - v327 != -3721 )
    v363 = 1;
  v326 = flag_9 * flag_4;
  if ( !is_mul_ok(flag_9, flag_4) )
    core::panicking::panic::h8705e81f284be8a5();
  if ( __OFSUB__(v326, flag_1) )
    core::panicking::panic::h8705e81f284be8a5();
  if ( v326 - flag_1 != 8037 )
    v363 = 1;
  v325 = flag_9 * flag_16;
  if ( !is_mul_ok(flag_9, flag_16) )
    core::panicking::panic::h8705e81f284be8a5();
  if ( !is_mul_ok(flag_11, v325) )
    core::panicking::panic::h8705e81f284be8a5();
  if ( flag_11 * v325 != 272832 )
    v363 = 1;
  v324 = flag_23 * flag_3;
  if ( !is_mul_ok(flag_23, flag_3) )
    core::panicking::panic::h8705e81f284be8a5();
  if ( __OFADD__(flag_15, v324) )
    core::panicking::panic::h8705e81f284be8a5();
  if ( flag_15 + v324 != 9792 )
    v363 = 1;
  v323 = flag_9 - flag_23;
  if ( __OFSUB__(flag_9, flag_23) )
    core::panicking::panic::h8705e81f284be8a5();
  if ( __OFSUB__(v323, flag_4) )
    core::panicking::panic::h8705e81f284be8a5();
  if ( v323 - flag_4 != -70 )
    v363 = 1;
  v322 = flag_5 - flag_21;
  if ( __OFSUB__(flag_5, flag_21) )
    core::panicking::panic::h8705e81f284be8a5();
  if ( __OFSUB__(v322, flag_8) )
    core::panicking::panic::h8705e81f284be8a5();
  if ( v322 - flag_8 != -63 )
    v363 = 1;
  v321 = flag_24 * flag_3;
  if ( !is_mul_ok(flag_24, flag_3) )
    core::panicking::panic::h8705e81f284be8a5();
  if ( __OFADD__(flag_0, v321) )
    core::panicking::panic::h8705e81f284be8a5();
  if ( flag_0 + v321 != 5359 )
    v363 = 1;
  v320 = flag_25 * flag_1;
  if ( !is_mul_ok(flag_25, flag_1) )
    core::panicking::panic::h8705e81f284be8a5();
  if ( __OFADD__(flag_17, v320) )
    core::panicking::panic::h8705e81f284be8a5();
  if ( flag_17 + v320 != 10483 )
    v363 = 1;
  v319 = flag_7 * flag_19;
  if ( !is_mul_ok(flag_7, flag_19) )
    core::panicking::panic::h8705e81f284be8a5();
  if ( !is_mul_ok(flag_2, v319) )
    core::panicking::panic::h8705e81f284be8a5();
  if ( flag_2 * v319 != 893646 )
    v363 = 1;
  v318 = flag_11 - flag_4;
  if ( __OFSUB__(flag_11, flag_4) )
    core::panicking::panic::h8705e81f284be8a5();
  if ( __OFADD__(flag_19, v318) )
    core::panicking::panic::h8705e81f284be8a5();
  if ( flag_19 + v318 != 93 )
    v363 = 1;
  v317 = flag_7 + flag_6;
  if ( __OFADD__(flag_7, flag_6) )
    core::panicking::panic::h8705e81f284be8a5();
  if ( __OFSUB__(v317, flag_10) )
    core::panicking::panic::h8705e81f284be8a5();
  if ( v317 - flag_10 != 136 )
    v363 = 1;
  v316 = flag_0 + flag_25;
  if ( __OFADD__(flag_0, flag_25) )
    core::panicking::panic::h8705e81f284be8a5();
  if ( __OFADD__(flag_10, v316) )
    core::panicking::panic::h8705e81f284be8a5();
  if ( flag_10 + v316 != 287 )
    v363 = 1;
  v315 = flag_12 + flag_5;
  if ( __OFADD__(flag_12, flag_5) )
    core::panicking::panic::h8705e81f284be8a5();
  if ( __OFSUB__(v315, flag_22) )
    core::panicking::panic::h8705e81f284be8a5();
  if ( v315 - flag_22 != 104 )
    v363 = 1;
  v314 = flag_4 * flag_7;
  if ( !is_mul_ok(flag_4, flag_7) )
    core::panicking::panic::h8705e81f284be8a5();
  if ( __OFADD__(v314, flag_12) )
    core::panicking::panic::h8705e81f284be8a5();
  if ( v314 + flag_12 != 8243 )
    v363 = 1;
  v313 = flag_1 - flag_22;
  if ( __OFSUB__(flag_1, flag_22) )
    core::panicking::panic::h8705e81f284be8a5();
  if ( __OFADD__(flag_4, v313) )
    core::panicking::panic::h8705e81f284be8a5();
  if ( flag_4 + v313 != 81 )
    v363 = 1;
  v312 = flag_19 * flag_11;
  if ( !is_mul_ok(flag_19, flag_11) )
    core::panicking::panic::h8705e81f284be8a5();
  if ( __OFSUB__(flag_8, v312) )
    core::panicking::panic::h8705e81f284be8a5();
  if ( flag_8 - v312 != -5503 )
    v363 = 1;
  v311 = flag_8 - flag_10;
  if ( __OFSUB__(flag_8, flag_10) )
    core::panicking::panic::h8705e81f284be8a5();
  if ( __OFSUB__(v311, flag_7) )
    core::panicking::panic::h8705e81f284be8a5();
  if ( v311 - flag_7 != -129 )
    v363 = 1;
  v310 = flag_20 + flag_22;
  if ( __OFADD__(flag_20, flag_22) )
    core::panicking::panic::h8705e81f284be8a5();
  if ( __OFADD__(flag_21, v310) )
    core::panicking::panic::h8705e81f284be8a5();
  if ( flag_21 + v310 != 224 )
    v363 = 1;
  v309 = flag_24 + flag_23;
  if ( __OFADD__(flag_24, flag_23) )
    core::panicking::panic::h8705e81f284be8a5();
  if ( __OFADD__(flag_12, v309) )
    core::panicking::panic::h8705e81f284be8a5();
  if ( flag_12 + v309 != 232 )
    v363 = 1;
  v282 = flag_15 - flag_9;
  if ( __OFSUB__(flag_15, flag_9) )
    core::panicking::panic::h8705e81f284be8a5();
  if ( __OFADD__(flag_4, v282) )
    core::panicking::panic::h8705e81f284be8a5();
  if ( flag_4 + v282 != 2 )
    v363 = 1;
  v255 = flag_9 * flag_15;
  if ( !is_mul_ok(flag_9, flag_15) )
    core::panicking::panic::h8705e81f284be8a5();
  if ( __OFADD__(flag_2, v255) )
    core::panicking::panic::h8705e81f284be8a5();
  if ( flag_2 + v255 != 5635 )
    v363 = 1;
  v228 = flag_24 + flag_14;
  if ( __OFADD__(flag_24, flag_14) )
    core::panicking::panic::h8705e81f284be8a5();
  if ( __OFADD__(flag_16, v228) )
    core::panicking::panic::h8705e81f284be8a5();
  if ( flag_16 + v228 != 210 )
    v363 = 1;
  v201 = flag_1 + flag_10;
  if ( __OFADD__(flag_1, flag_10) )
    core::panicking::panic::h8705e81f284be8a5();
  if ( __OFSUB__(v201, flag_12) )
    core::panicking::panic::h8705e81f284be8a5();
  if ( v201 - flag_12 != 125 )
    v363 = 1;
  v174 = flag_18 - flag_1;
  if ( __OFSUB__(flag_18, flag_1) )
    core::panicking::panic::h8705e81f284be8a5();
  if ( __OFSUB__(v174, flag_5) )
    core::panicking::panic::h8705e81f284be8a5();
  if ( v174 - flag_5 != -111 )
    v363 = 1;
  v147 = flag_12 - flag_14;
  if ( __OFSUB__(flag_12, flag_14) )
    core::panicking::panic::h8705e81f284be8a5();
  v146 = v147 - flag_7;
  if ( __OFSUB__(v147, flag_7) )
    core::panicking::panic::h8705e81f284be8a5();
  if ( v146 != -163 )
    v363 = 1;
  HIDWORD(v119) = flag_1 + flag_5;
  if ( __OFADD__(flag_1, flag_5) )
    core::panicking::panic::h8705e81f284be8a5();
  LODWORD(v119) = HIDWORD(v119) - flag_16;
  if ( __OFSUB__(HIDWORD(v119), flag_16) )
    core::panicking::panic::h8705e81f284be8a5();
  if ( (_DWORD)v119 != 158 )
    v363 = 1;
  if ( v363 )
  {
    v87 = &off_55FC0;
    core::fmt::Arguments::new_v1::hfd3f880f4c7be2d8(v366, &off_55FC0, 1LL, &unk_45140, 0LL);
  }
  else
  {
    v87 = &off_55FD0;
    core::fmt::Arguments::new_v1::hfd3f880f4c7be2d8(v365, &off_55FD0, 1LL, &unk_45140, 0LL);
  }
  std::io::stdio::_print::h7035045a22bdb588();
  core::ptr::drop_in_place$LT$alloc..vec..Vec$LT$char$GT$$GT$::h23b141f84cc9b646(
    (int)v364,
    (int)v87,
    v88,
    v89,
    v90,
    v91,
    v119,
    v146);
  return core::ptr::drop_in_place$LT$alloc..string..String$GT$::h813c59c7958382cd(v359);
}
```
- The only hard thing about this challenge is that you have to know how input is being processed
- Each character in the input is assigned to some variables with `flag_0 = *(_DWORD *)_$LT$alloc..vec..Vec$LT$T$C$A$GT$$u20$as$u20$core..` type of pattern,
then used some mathematical calculation on those values and compare them to some constant values (Like a system of equations)
- Also it is worth to mention how `v119` being accessed. `HIWORD`(the higher 2 bytes) of it is being calculated first then `LOWORD` (the lower 2 bytes). For example:
 + We have v119 = 0xFFFFFFFF (v119 here is a DWORD = 4 bytes)
 + If HIWORD(v119) = 0x0012 then v119 = 0x0012FFFF
 + If LOWORD(v119) = 0x0012 then v119 = 0xFFFF0012
- With these pieces of information, we can write a python script to solve this challenge

```python
from z3 import *

flag = [BitVec(f'x[{i}]', 8) for i in range(0x1A)]
s = Solver()

for i in range(0x1A):
    s.add(flag[i] >= 0x20)
    s.add(flag[i] <= 0x7F)

v332 = flag[19] * flag[11]
s.add(flag[4] * v332 == 391020)

v330 = flag[13] * flag[8]
s.add(flag[22] * v330 == 567720)

v329 = flag[22] * flag[0]
s.add(flag[15] + v329 == 4872)

v328 = flag[0] + flag[8]
s.add(flag[11] + v328 == 199)

v327 = flag[22] * flag[12]
s.add(flag[13] - v327 == -3721)

v326 = flag[9] * flag[4]
s.add(v326 - flag[1] == 8037)

v325 = flag[9] * flag[16]
s.add(flag[11] * v325 == 272832)

v324 = flag[23] * flag[3]
s.add(flag[15] + v324 == 9792)

v323 = flag[9] - flag[23]
s.add(v323 - flag[4] == -70)

v322 = flag[5] - flag[21]
s.add(v322 - flag[8] == -63)

v321 = flag[24] * flag[3]
s.add(flag[0] + v321 == 5359)

v320 = flag[25] * flag[1]
s.add(flag[17] + v320 == 10483)

v319 = flag[7] * flag[19]
s.add(flag[2] * v319 == 893646)

v318 = flag[11] - flag[4]
s.add(flag[19] + v318 == 93)

v317 = flag[7] + flag[6]
s.add(v317 - flag[10] == 136)

v316 = flag[0] + flag[25]
s.add(flag[10] + v316 == 287)

v315 = flag[12] + flag[5]
s.add(v315 - flag[22] == 104)

v314 = flag[4] * flag[7]
s.add(v314 + flag[12] == 8243)

v313 = flag[1] - flag[22]
s.add(flag[4] + v313 == 81)

v312 = flag[19] * flag[11]
s.add(flag[8] - v312 == -5503)

v311 = flag[8] - flag[10]
s.add(v311 - flag[7] == -129)

v310 = flag[20] + flag[22]
s.add(flag[21] + v310 == 224)

v309 = flag[24] + flag[23]
s.add(flag[12] + v309 == 232)

v282 = flag[15] - flag[9]
s.add(flag[4] + v282 == 2)

v255 = flag[9] * flag[15]
s.add(flag[2] + v255 == 5635)

v228 = flag[24] + flag[14]
s.add(flag[16] + v228 == 210)

v201 = flag[1] + flag[10]

v174 = flag[18] - flag[1]
s.add(v174 - flag[5] == -111)

v147 = flag[12] - flag[14]
v146 = v147 - flag[7]
s.add(v146 == -163)

v119 = 0xFFFFFFFF
v119 = ((v119 & 0x0000FFFF) << 16) + (flag[1] + flag[5])

v119 = v119 - flag[16]
s.add(v119 == 158)
if(s.check() == sat):
    x = ''
    for i in range(len(flag)):
        last = int(str(s.model()[flag[i]]))
        x += chr(last)
else:
    print("Failed")
print(x)
```

![image](https://github.com/user-attachments/assets/fd91b59a-d54e-43c1-a4ea-334373ef80a4)


**Flag:** `CSCTF{ruSt_15_c00l_r1gHt?}`
