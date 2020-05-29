import gmic
import bpy
gmic.default_parameters = {'afre_edge': '1,1,1,1', 'fx_gmicky': '0', 'afre_contrastfft': '75,50,1', 'fx_hnorm': '1,50,0', '-srand': '781123', 'afre_gleam': '3,50', 'afre_vigrect': '50,75,10,50,50', 'afre_softlight': '100,0', 'afre_vigcirc': '90,75,50,50', 'mc_rooster': '50,0,255,255,255,255,1', 'mc_kookaburra': '50,0,255,255,255,255,1', 'mc_paw': '50,0,255,255,255,255,1', 'fx_array_mirror': '1,0,0,2,0,0,0', 'fx_array_fade': '2,2,0,0,80,90,0,0', 'Annular_Steiner_Chain_Round_Tile': '800,1,0,0,100,0,100,12,0,1,0,0,0,255,0,255,255,0,127,0,0,255,127,0', 'Cercles_Concentriques_A': '800,1,6,0,0,90,1,1,50,1,1,0,0,0,255,0,0,0,0,5,0,0,0,255,255,255,255,0,255,255,0,0,255,0,255,255,255,255,0,255,255,0,1,0,5,0,0', 'fx_imagegrid': '10,10', 'fx_array': '2,2,0,0,0,0', 'array_random': '5,5,7,7', 'fx_ministeck': '8,64,8,2,100,0.3,0', 'samj_Carres_Noirs': '128,40,7,0,0,0,0,255,2,96,96,96,255,2,255,255,255,255,0,2,0', 'Cercles_Concentriques_A_en': '800,1,6,0,0,90,1,1,50,1,1,0,0,0,255,0,0,0,0,5,0,0,0,255,255,255,255,0,255,255,0,0,255,0,255,255,255,255,0,255,255,0,1,0,5,0,0', 'fx_dices': '2,24,1', 'samj_Moirage_Spline': '0,0,0,255,8,0,-50,50,-50,50,0,0,0,0,0,255,8,0,-50,50,-50,50,0,0', 'samj_en_Coeurs_Hearts_002': '16,100,0,0,1,0,255,255,255,255,0,0,0,1,1', 'fx_imagegrid_triangular': '10,18,0,255,255,255,128', 'fx_taquin': '7,7,0,50,5,0,0,0,0,255,0', 'samj_Bulles_Colorees': '64,64,64,255,8,0,0,3,0,0,0,0,0,0,0,0,255', 'fx_puzzle': '5,5,0.5,0,0,0.3,100,0.2,255,100,0,0,0,0,0,0', 'fx_rotate_tiles': '5,5,15,3,3,1.8', 'samj_Ellipses_Colorees': '64,64,64,255,8,8,0,0,0,0,0,255', 'samj_Losanges_Colores': '64,64,64,255,8,0,0,0,1.5,0,1,0,0,0,0,0,255,0', 'fx_brushify': '7,0.25,4,64,25,12,0,2,4,0.2,0.5,30,1,1,1,5,0,0.2,1', 'samj_Contour_Drawings_en': '5,0,2,0,0,5,10,0.8,0,1.1,10,0,1', 'samj_Pixelisation_Contours': '0.5,0,20,8,0,0,1,0,10,0.8', 'samj_Pointes_De_Diamants_Colorees': '64,64,64,255,8,0,0,1.5,0,0,0,0,0,0,0,255,0', 'gtutor_fpaint': '0.5,0.5,0.0,0,45.0,0.5,0.5,0.5,0', 'fx_parameterize_tiles': '10,10,0', 'fx_shift_tiles': '10,10,10,1', 'fx_graphic_boost4': '1.25,2,0,0.15,14,0,1,0.5,0.45,2,0,1,0,1,1,1,0.5,0.45,1', 'gcd_aurora': '6,1,0', 'fx_crayongraffiti2': '300,50,1,0.4,12,1,2,2,0', 'fx_cpencil': '1.3,50,20,2,2,1,0', 'Engrave_colore_en': '0,0.5,4,0,8,40,0,25,1,2,0,0,0,255,255,255', 'fx_neon_alpha': '0,0.45,40,60,0,2,1.15,20,0.4,0.1,2.25,5,0.2,0.1,2.25,2,1', 'afre_sharpenfft': '15,1', 'fx_tk_photoillustration': '0,0.25,0,0.30,0.50,0.50,1.00,0,5.00,0,1,0,0,1,0,0,1.2,98.5,5,0.5,0,0,0,0,0,1,0', 'fx_dreamy_watercolour': '0,0.3,40,60,0,1,50,0,10,2,1,1,0.5,10,0,0,7,1,3,1,1,1,1,1,11,1,25,5,1,10,1,0,0,1,0.5,0,8,1,0,128,128,128,0.5,1,8,0.2,1,1,0,27,0.75,0,1,20,40,40,1,2,1.25,0,2,1,27,1', 'samj_Edges_And_LIC': '0,200,0,0,0,15,8,127,255,0,0,1,20,0.2,0,14,1', 'samj_Angoisse': '1,5,0,5,100,2,4,1,250', 'mc_dragonfly': '50,0,255,255,255,255,1', 'fractalize': '0.8', 'samj_Couleurs_Rayees': '0,30,0,100,4,4,0,2,0.7,0', 'samj_en_Texture_Granuleuse': '0,20,80.0,0,0,0', 'Annular_Steiner_Chain_Round_Tile_en': '800,1,0,0,100,0,100,12,0,1,0,0,0,255,0,255,255,0,127,0,0,255,127,0', 'samj_Fond_Brosse': '3,1', 'fx_illustration_look': '100,0,0,0,0', 'fx_MorphoPaint': '1,18,2,25,100,230,8,3,4,0.5,2,0.5,200,1,1,1,1,1,1,1,1,0', 'fx_array_color': '5,5,0.5', 'samj_Isophotes_Vers_Aquarelle': '16,0.5,4,0,1,10,1,0,0,0,0,1,10,10,4,3,251,237,206,1', 'fx_pastell': '0.6,1,0,20,30,300,1,30,1,1,0.5,0,0,10,3,0,9,3,0,12,0', 'samj_Barbouillage_Paint_Daub_en': '2,2,100,0.2,1,4,1,0,8', 'fx_SimpleNoiseCanvas': '0,3,2,5,5,0,255,0,2,0,0,0,1,0,255,255,255,255,0', 'samj_Scintillements_Colores_en': '64,64,64,255,8,8,0.5,384,12,0,0,0,0,0,0,0,255,0', 'warhol': '3,3,2,40', 'samj_Plasmic_V2': '2,4,10,2,0.02,8,0,0,0,0,0,0,255', 'fx_pdithered': '1,1,0,0,20,1,0,1,0', 'fx_imagegrid_hexagonal': '32,0.1,1', 'fx_autofill_lineart': '90,1,8,0,0', 'Engrave_colore': '0,0.5,4,0,8,40,0,25,1,2,0,0,0,255,255,255', 'samj_Contour_Epais': '1,0,5,1,5,5,10,0.8,2,1', 'samj_Color_EdgesO_Engrave': '0,50,9,1,2,50,0,8,40,0,0,1,0,0,0', 'fx_montage': '0,"V(H(0",1,0.5,0,0,0,0,0,255,0,0,0,0,0', 'fx_gcd_layeretch': '11,4,12,0.12,100,8.5,5,0,0,3,1,1,0', 'samj_fond_broderie': '8,2,0,1,1', 'samj_Diff_Tensors_Blend': '10,5,1,0.15,1,0,3,1,0,3,1', 'samj_Coeurs_Hearts_002': '16,100,0,0,1,0,255,255,255,255,0,0,0,1,1', 'fx_channels2layers': '0', 'samj_Impressions': '10,5,5,1,1,0,2,0,1,5,0,5,100,2,4,1,250,1.2', 'samj_Gris_Raye': '0,30,0,100,4,4,255,1', 'samj_Moirage_Spline_XY': '0,0,0,255,8,0,-50,50,-50,50,0,0,0,0,255,8,0,-50,50,-50,50,0,0', 'fx_tk_colortemp': '0,0,0', 'samj_texture_coloree': '"A",0.7,200,125,50,5,5,45,200,4,0.2', 'samj_TensorTest': '0.3,0.9,0.6,1.1,0,0,20,32,20,2,1,0,2', 'fx_normalize_tiles': '25,25,0,255,11', 'fx_hsv_equalizer': '0,180,40,0,0,0,180,40,0,0,0,180,40,0,0,0', 'samj_texture_coloree_en': '"A",0.7,200,125,50,5,5,45,200,4,0.2,1,10,1,1', 'iain_hue_light_dark_p': '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,255,100,255,0,0,0', 'samj_Angoisse_en': '1,5,0,5,100,2,4,1,250', 'fx_whirling_lines': '30,6,0,0,0.45,40,60,0,0,30,0,3,3', 'fx_recolorize': '2,0.2,0', 'samj_Variations_RVB': '50,50,0,6,0,0,180,90,45,0,1,0', 'fx_ColorAbstractionPaint': '5,10,1,0,1,0,1,0,0,0,0,0,0,0', 'fx_colorize_lineart_smart': '0,95,0,0,1,24,200,0,75,2,60,20,90,1,10,1,0', 'fx_gcd_norm_eq': '0.5,0.5,2,0', 'fx_tk_vintage': '2,0.85,0.7,80,200,5,147,26,161,0.3,235,220,176,0.4,190,181,108,0.2,0,0,100,0,0.3,25,0,0', 'fx_dreamsmooth': '3,1,1,0.8,0,0.8,1,24,0', 'XY_hardsketchbw_samj_en': '0.2,300,50,1,0.1,20,0,0,0,0,180,40,160,255,0', 'fx_ink_wash': '0.14,23,0,0.5,0.54,2.25,0,2,6,5,20', 'samj_Coloriage': '612,255,2,6,2,0,0,0,255,0', 'samj_Flamboyance_Test': '65,28,9.25,0.3,0,1,1.1,10,12,2,0,0,1,0,150,0.42,0.85,0.6,7.83,0.68,19,2.65,0,1,1,3,200,20,0.1,1.5,8,1,3,1,0,20,0,0,0,0', 'fx_remove_scratches': '72,2,4,3,0', 'samj_scintillements': '0,5,0,1,20,2,6,20,5,45,2,6,5,20,1,7,0,0', 'fx_graphic_novelfxl': '0,2,6,5,20,0,0.62,14,0,1,0.5,0.78,1.92,0,0,0,1,1,1,0.5,0.8,1.28', 'samj_Quelques_Isophotes_B': '16,100,0,0,4', 'samj_Color_Palettes': '50,50,0,6,24,0,0,180,90,45,1,3,2,1', 'jl_colorgrading': '0.,0,1,1,0,0,0,0,0,0,1,0,0,0,70,0,0,0,0,0,70,180,0,1,0,0,0', 'fx_otsu_hessian_blend': '4,0,1,27,1,0', 'fx_corvo_painting_5': '35,10,10,0.5,50,0.3,50,2,5,1', 'fx_darken_sky': '.75,5,0,1,0,0', 'fx_decompose_channels': '7,0,0,1', 'samj_Plasmic': '0,1.1,2,40,0,0,0,0', 'fx_conformal_maps': '8,1,0,1,0,0,0,0,0,3,0,0,1024,1024', 'gcd_hsv_select': '0,0.5,1,180,0.5,0.5,2,2,18,0,0,0', 'gcd_hsl': '1,0,0,180,0.2,0,1,1,0', 'samj_Barbouillage_Paint_Daub': '2,2,100,0.2,1,4,1,0,8', 'fx_equirectangular2nadirzenith': '0', 'iain_rgb_tone': '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,255,255,255,255,255,0', 'samj_At06A_2017_VarCouleurs': '1,0,100,0,0', 'samj_Couleurs_Rayees_2': '0,30,0,100,4,4,255,1', 'samj_Random_Small_Deformations': '10,5,3', 'iain_tone_presets_p': '0,100,0,0', 'fx_gcd_transfer_colors_patch': '6,3,5,5,0,0', 'samj_fx_sketchbw_modifie': '3,45,180,30,1.75,0.02,0.5,0.75,0.1,0.7,3,6,0,1,4,0,1234,0,2,100,0.2,1,4,1,0', 'fx_reflect': '50,1,110,160,190,64,0,1.5,0,-3.30,7,1.5', 'samj_Colored_Outlines': '0,2,8,0,0,0,0,0,255', 'samj_Carte_De_Repoussage': '30,1,0,0', 'samj_Pointillisme_B': '1,0,90,3,1,1,0,0,0,255', 'ripple': '10,20,2,0,0', 'samj_Quelques_Isophotes': '10,10,1,0.02,8', 'samj_Contours_Colores': '1.1,2,40,0,0', 'samj_Test_Skeletik': '10,1,0,0,0,3,1,0,0,0,255', 'samj_Cercle_Polaire': '1,0,0,1,0,0,2,0,0,0,50,50', 'samj_Skeletation': '2,100,100,0,0,1', 'samj_Test_Mauvais_Contours': '0,0,0,2,1,0,255,0,255,0,0,3,1', 'fx_watercolor': '1.8,0.1,1,80,0,0.5,0,0,0,2,0,2,4,2,0,3,3,2,0,4,2,0,0,0,0,0', 'fx_seamcarve': '85,100,15,0,1', 'fx_apply_YCbCrcurve': '0,-1,128,-1,128,-1,128,-1,128,-1,128,255,1,0,0', 'fx_auto_gnarl': '3,0.45,40,60,0,1,1,2,4,6,5,20,1,2.5,0.5,2,2,3', 'fx_colorize_lineart': '0,1,0,0.05', 'fx_map_sphere': '512,512,90,0.5,0,0,20,0,0,0,0.5', 'fx_crease': '30,10,3', 'fx_drop_water': '0,20,2,80,0,3,35,10,1,0.5,0.25,0.5,0.75,0.05,0.15,1', 'engrave_modifie': '0,0.5,4,0,8,40,0,25,1', 'fx_jr_spiral_transform': '0,0,0,0,0', 'raindrops': '80,0.1,1,0', 'deform': '10', 'samj_NB_EdgesO_Engrave': '0,50,9,1,2,50,0,8,40,0,0,1', 'fx_square_circle': '0,1,0,0,0,0,0', 'sawtoother_yuv8': '1,0,0,1,1,0,1,0,0,1,1,0,1,0,0,1,1,0,0,2,0', 'fx_yag_soften': '0,0,0', 'iain_cmyk_tone_p': '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,255,255,255,255,255,0,0', 'water': '30,1.5,45', 'fx_frame_blur': '30,30,0,5,0,0,128,128,128,0,5,255,255,255,2,2,1,0,0.5,0.5,0', 'fx_jr_smooth_eq': '8,2,0,3,2,1.5,0,4,2,2,0,5,2,2,0,6,2,2,0,7,2,2,0,3,2,0,0,0,1,1,0', 'fx_customize_clut': '100,0,10,0,0,0,0,0,0,0,8,0.5,1,0,0,0,0,0,0,1,255,255,255,255,196,128,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0', 'fx_simulate_grain': '0,1,0.2,100,0,0,0,0,0,0,0,0', 'frame_cube': '3,0,0,0,0,0,0', 'fx_streak': '255,0,0,255,0,0,3', 'fx_frequency_representation': '3,256,0,40,0', 'fx_blur_bloom_glare': '1,2,5,0,0,0,0,0,3,0.5,7,0', 'fx_superstreak': '10,10,3,0.50,0.50,10,30', 'fx_tk_metallic': '1,0,0,0', 'fx_frame_fuzzy': '5,5,10,1,255,255,255,255', 'fx_butterworth_bp': '3,2,0,4,2,0,0,0,1,1,0', 'fx_watermark_visible': '"©', 'Saturation_EQ_p': '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0', 'fx_frame_mirror': '10,10,50,50,0,0,0,0,0.75', 'fx_gcd_crt': '1.8,1.8,0,0', 'fx_morpho': '0,5,0,0,0,0,0', 'fx_frame_painting': '10,0.4,6,225,200,120,2,400,50,10,1,0.5,123456,0', 'fx_zonesystem': '1,10,1,1,0,255,0', 'samj_Zones_Grises_en': '3,0,3,4,1', 'fx_bitplane8': '0,1,0,0', 'fx_frame_pattern': '10,1,1,1', 'samj_Contours_Arrondis': '1,3,5,10,0,0', 'fx_jfif_xt': '50,8,8', 'iain_constrained_sharpen': '.75,2,1,5,0,11,1', 'fx_frame': '0,100,0,100,10,10,0,0,0,255,1,255,255,255,255', 'samj_Scintillements_Colores_Contours': '0,8,0,8,8,1,768,12,0,0,0,0,0,0,0,255', 'samj_Degradations_Path_Solidify': '0,0,0,0,0,2,10,1,0,0,1,75,0,20', 'jeje_dehaze': '5,1,.2,1,0,0,0,0,0', 'fx_frame_round': '6,20,0.1,0,255,255,255,255,0,0.1,3', 'fx_apply_Labcurve': '0,-1,128,-1,128,-1,128,-1,128,-1,128,255,1,0,0', 'fx_pixelsort': '1,0,0,1,0,100,0,0,0', 'fx_tk_dri': '0,0,0,1,0.5,1,1,0', 'souphead_droste10': '40,100,1,1,1,0,0,0,0,0,1,10,1,0,90,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0', 'fx_frame_smooth': '10,10,0.25', 'samj_Random_Plasma': '0,80', 'fx_highpass': '5,2,0,0,0', 'fx_symmetrizoscope': '4,0,3,0', 'fx_old_photo': '200,50,85', 'fx_row_shift': '0,0,0.5,0,0.5,3,0', 'fx_LCE': '80,0.5,1,1,0,0', 'gcd_jpeg_smooth': '1,1,0,0', 'fx_polaroid': '10,20,0,0,3,0,20,50,70,95', 'samj_Ellipses_Inpaint': '0,0,0,8,8,2,0,10', 'jeje_normalize_local_variance': '50,5,5,1,0,0', 'gcd_layers': '100,0,1,0,0,0,0,0,1,0,0,1', 'samj_At06A_2017_frame_painting': '10,0.4,6,127,127,127,2,400,50,10,1,0.5,123456,35,1,1,1,0,100', 'samj_Zones_Grises': '3,0,3,4,1', 'make_up': '15,4,0,0,0', 'gcd_balance_lms': '1,1,1,0,0,0', 'fx_vignette': '70,70,95,0,0,0,255', 'sawtoother_cmy_k': '1,0,0,1,1,0,1,0,0,1,1,0,1,0,0,1,1,0,0,1,0,0,1,1,0,0,2,0', 'fx_tk_mask': '0,0,0,255,0,1,0,0,1,0', 'gcd_fx_local_fmean': '15,0,0,5,0', 'fx_fourier': '1,1', 'sawtoother_hsx': '1,0,0,1,1,0,1,0,0,1,1,0,0,1,0,0,1,1,0,0,2,0', 'fx_tk_portrait': '0,100,1,5,20,3,20,10,0,0,1,2,25,2,250,180,150,255,0,0,1,1.5,10,1,0,0,1,1,0,0', 'fx_watermark_fourier': '"(c)', 'tran_multi_threshold': '50,100,150,200,9,0,1,175,42,27,101,101,101,174,165,131,247,228,160', 'sawtoother_lab8': '1,0,0,1,1,0,1,0,0,1,1,0,1,0,0,1,1,0,0,2,0', 'iain_pyramid_processing': '4,50,.5,0,0', 'gcd_normalize_brightness': '0,10,0,3,0,0', 'gcd_anti_alias': '60,0.3,50,0', 'sawtoother_lch8': '1,0,0,1,1,0,1,0,0,1,1,0,1,0,0,1,1,0,0,2,0', 'samj_Antialias_Wavelet': '40,0,127,255,1,60,1,1,1', 'fx_gcd_quicktone': '1,4,20,0,3,1', 'gcd_auto_balance': '30,0,0,1,0', 'sawtoother_rgb': '1,0,0,1,1,0,1,0,0,1,1,0,1,0,0,1,1,0,0,2,0', 'jeje_hessian_sharpen': '3,1,1,0,0', 'gcd_recol': '-14,14', 'gcd_blend_feather': '100,0.5,2,0,0', 'sawtoother_srgb': '1,0,0,1,1,0,1,0,0,1,1,0,1,0,0,1,1,0,0,2,0', 'samj_Wavelet_Sharpen_Test_en': '0,0', 'gcd_sharpen_gradient': '0.5,2,0,0', 'gcd_comp_blur': '2,3,1,100,1,0,0', 'sawtoother_xyz8': '1,0,0,1,1,0,1,0,0,1,1,0,1,0,0,1,1,0,0,2,0', 'jeje_whiten_frequency': '50,0,0', 'gcd_sharpen_tones': '1,128,0,0', 'fx_gcd_cumul_math': '0,1,1,0,0', 'sawtoother_ycbcr': '0,1,0,0,1,1,0,1,0,0,1,1,0,1,0,0,1,1,0,0,2,0', 'fx_split_details_alpha': '6,10,1,5,0', 'gcd_srotate': '0,50,50,1,1,6,0.6,0', 'gcd_depth_blur': '0,15,0.25,2,4,0,1', 'sawtoother_yiq8': '1,0,0,1,1,0,1,0,0,1,1,0,1,0,0,1,1,0,0,2,0', 'fx_split_details_gaussian': '6,10,1,0', 'gcd_emboss': '128,0', 'gcd_temp_balance': '0,0,1,0', 'iain_easy_skin_retouch': '7,2,.7,1,1,.7,.6,.5,.5,.5,0', 'fx_split_details_wavelets': '6,0,0', 'gcd_geometric_balance': '0', 'gcd_unquantize': '6,1,1,5,15', 'exfuse': '1,0.6,0,0.5,1,5', 'jeje_spotify': '1,1,1,1,11,0', 'gcd_upscale_box': '0,0,0', 'gcd_infomap': '0', 'exfusion5': '0,.2,0.2,1,0,0', 'iain_texture_enhance_p': '2,2,30,0,11,0,0', 'gcd_ebwarp': '0.5,1', 'gcd_upscale_noise': '16,2', 'fft_tile': '500,128,0', 'gcd_tone_enhance': '0,1,0,1,128,0,1,0.5,0,0,4,0,0', 'gcd_warpmap': '5,0,0,0,0', 'MS_Patch_NR3': '1.3,0,0,0,3,5,1,0,0,0,0,0', 'fill_holes': '11,21,5,0,0,1', 'samj_Wavelet_Sharpen_Test': '1', 'fx_gb_cfx': '10,0,0,0,0,0', 'ms_patch_smooth': '10,5,3,5,0,1,1,7,5,4,3,2,1,1,1.3,0', 'iain_descreen2': '3,-10000,10', 'jpr_phasecongruence': '45,1,50,1', 'fx_gb_lb': '10,7,0', 'ms_smooth': '0,0,0,0,0,0,2,0,2,0', 'iain_halftone_shapes': '100,0,0,0,0,0,0', 'hedcut': '0.5,0.5,0.5,0.0,0.5,0,1,0', 'jpr_remove_blocks1': '4,3,70', 'nr5': '1.6,5,1,1,.75,3,0,.75,.5,0,1,1,100,0,-100,0,1.3,0', 'iain_hearttone': '100,0', 'jpr_shapes_gradient': '2,0.25,0.001,100', 'iain_png_processing': '4,0,0,0,3,3,0,.75,2,1,5,0,0,1,1', 'iain_2d_scopes': '1,2,2,6,512,2048,1,0,0,0,0', 'iain_demosiac': '0', 'jpr_specularbumps': '270,1,13,0,80,0.1,0.1,0', 'iain_smooth_tutorial': '1000,0.5,1,0.6,1.1,0,0', 'simplelocalcontrast_p': '16,2,0,1,1,1,1,1,1,1,1,0', 'iain_denoise_2019_beta3': '1,0,0,0,0.5,1,0,5,3,0,3,0,.5,4,0', 'jpr_warpfromthreshold': '170,2,10,2', 'automixer': '0,0', 'iain_fx_skin_mask': '55,200,0,0,0,1', 'iain_remove_pattern': '3,3,3,0,4,128,1,0', 'fx_mesh_blend': '0,3,0,0,0,0', 'iain_brown_spot_clean': '1,2', 'iain_smartdemos': '0,1.5,2', 'iain_star_burst': '254,50,5,45,2,0,0', 'iain_CA_correction': '0,0,2,0,3', 'fx_align_layers': '0,0.7,0,0', 'star_tone': '100', 'iain_detect_moire': '50,5,9,30', 'iain_unindex': '30,20,1,50,50', 'fx_blend_average_all': '0', 'iain_sub_cast': '5,20,250', 'fx_tones2layers': '3,85,170,0.5,0', 'iain_weightmap': '1,40', 'fx_blend_edges': '1,0.8,0', 'iain_turbulent_halftone': '15,20,0,1,512,0.75,0,0,0', 'fx_contrast_swm': '2,0,1', 'iain_iains_nr': '3,3,1,0,0,0,1,0,0,0,1.35,0,0', 'fx_blend_fade': '1,0,0,5,0,0,0,0,0,0,"cos(4*pi*x/w)', 'mc_flip': '50,0,255,255,255,255,1', 'fx_dodgeburn': '15,1.5,25,10,40,1.5,25,10,0,0,10,0', 'iain_iid_demosaic': '1,1,1,0,0', 'fx_blend_median': '0', 'mc_information': '50,0,255,255,255,255,1', 'fx_drop_shadow': '3,3,1.8,0,0,0', 'fx_blend_seamless': '0,0,25,0,0', 'luminance_nr_two': '10,1,1,.8,.7,.6,.5,.4,.3,1200,64,0,0,0,0,0,0,0,0,0,0,0', 'mc_mail': '50,0,255,255,255,255,1', 'fx_drop_shadow3d': '0,0,0,0,1,1,2,0.5,0,0,0,200,0', 'mc_phone': '50,0,255,255,255,255,1', 'iain_minimum_chroma_demosaic': '0,2,0', 'fx_blend': '6,0,100,1,"1/2', 'fx_light_patch': '5,0.7,2.5,0', 'mc_shopping_cart': '50,0,255,255,255,255,1', 'iain_moire_removal': '5,5,0', 'fx_split_colors': '50,16,1,0', 'samj_Ombre_Portee': '0,0,0,128,0,0,0,0,255,127,127,127,255,2,2,255,255,255,255,0.1', 'iain_moire_removal_NP': '5,5,0', 'jeje_zernike_preview': '50,50,50,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0', 'fx_fade_layers': '10', 'samj_Ombre_Portee_B': '16,128,0,1,16,1,0,0,127,127,127,255,2,2,2,2,255,255,255,255', 'ms_nlmeans_c_noise2_p': '3,1,0,0,0,0,0,10,2,4,2,7,0,0,0,0', 'append_tiles': '0,0', 'jpr_colourillusion': '2,25', 'samj_Ombre_Portee_C': '32,8,16,192,0,1,16,1,0,0,96,96,96,255,2,2,2,2,255,255,255,255', 'fx_morph_layers': '10,0.2,0.1,0', 'jpr_coltexindex': '5,55,55,45,45,1,1,0,0.05,0.5,0.95,0.5,1,2,0.7', 'ms_patch_c': '5,1,1,5,4,3,2,1,1,1.3,0.375,.5,0.125,0', 'samj_Ombre_Portee_D': '16,64,64,2,1,16,5,1,-32,4,1,2,2,2,255,255,255,255', 'fx_apply_multiscale': '4,25,100,0,3,0.5,0.5,0,0,0.5,0.5,0,"",0,0', 'MS_Patch_NR': '1.3,0,0,0,3,5', 'jpr_decimate': '0.375,2', 'fx_shadow_patch': '0.7,0', 'Lylejk_Wicker_2': '50,50,1,50,50,1,1,12,10,5,1,1,0,0,0,255,150,0.54,0.85,0.6,7.83,0.68,19,2.64,0,1,3,0,0.29,28.7,100,0,0,1,10,20,0.1,1,10,12,2,40,0.7,0.3,0.6,1.1,0.8,30,2,0,1,3,1,0,16,1,0', 'fx_stroke': '3,50,0,2,1,100,0,0,255,255,255,255,255,255,255,255,0,0,0,0,0,0,0,0,1,0', 'jpr_gradient_smooth': '0,1.5', 'fx_slice_luminosity': '1,1,2,1,0,64,0,0,1,64,128,0,0,0,128,192,0,0,0,192,255,0,0', 'Lylejk_Woven': '19.6,32.4,1,0,0,19.6,32.4,1,0,0,12,10,5,1,1,0,0,0,255,19.6,32.4,1,0,0,19.6,32.4,1,0,0,150,0.61,0.85,0.6,7.83,0.68,19,2.64,0,1,1,0,0.29,37.2,100,0,0,2,0,16,0', 'split_tiles': '3,3,0', 'jpr_orientedthinning': '5,15,1,0,0', 'fx_blend_shapeaverage': '1,0,0', 'fx_split_luminance': '1,1,1,0,0', 'garagecoder_lylejk_samj_points_outlines': '0,0.05,10,0.12,0,0,2,0', 'fx_crystal_background': '10,25,0,100,1', 'fx_lylejk_stencil': '5,10,3,0', 'fx_hue_overlay_masks': '0,5', 'fx_MappedSmooth': '0,0,0,300,1,0', 'samj_Degrades_HSL_TSL': '4,800,240,240,40,255,120,40,240,255,0,0,0,360,100,100,0,0,0,718,75,100,0,100,0,0,0,0', 'Lylejk_Luma_Invert': '1,0', 'fx_fix_HDR_black': '20,25,50,200,0,0', 'mc_barbed_wire': '50,0,255,255,255,255,1', 'jeje_fibers': '10,50,10,0', 'Lylejk_Quantize_Wicker': '16,50,50,0,16,10,5,1,1,0,0,0,255,1,10,10,153,0,2,10,20,0.1,1,0', 'fx_noisepainting': '0,0,0,5,2.5,1.5,50,1,0', 'mc_crosshair': '50,0,255,255,255,255,1', 'samj_Formes_Couleurs_Variees_Dans_Image': '0,0,0,0,0,192,128,64,255,1,1,1,0,0,127,255,0,0,0,0,1', 'Lylejk_Ribbon': '150,0.42,0.85,0.6,7.83,0.68,19,2.64,0,1,2,16,3.44,0,3,0.79,0.72,4.97,1.70,150,0.42,0.85,0.6,7.83,0.68,19,2.64,0,1,2,0,0.32,43.1,100,0,2,1.15,5,1,0', 'fx_SmoothSketch': '1,6,0.8,0.3,0.3,0,1000,0,50,10,2,0.6,0.55,1,0', 'fx_cupid': '75,0,255,255,255,255,1', 'fx_marble': '.5,1,0,0,.4,.6,.6,1.1,0,100', 'lylejk_test_TRW': '50,50,1,16,10,5,1,1,0,0,0,255,50,50,1,1,1.8,10,153,150,0.42,0.85,0.6,7.83,0.68,19,2.64,0,1,1,0,0.5,10.5,100,0,0,0.5,10.5,100,0,1.15,5,1,0.68,0.5,10.5,100,0,0,1,10,1,0,0', 'fx_gear': '75,12,15,0,40,0,255,255,255,255,1', 'fx_DemoVecRot': '0', 'samj_Marbre_en': '1,1,8,5,0.2,0,0,0,140,120,220,0,3,1', 'Lylejk_Wicker': '10,10,153,150,0.42,0.85,0.6,7.83,0.68,19,2.64,0,1,1,0,0.5,10.5,100,0,0,0.5,10.5,100,0,1.15,5,1,0.68,0.5,10.5,100,0,0,1,10,1,0,0', 'fx_WarpTest': '0,0,0,1,0', 'fx_heart': '75,0,255,255,255,255,1', 'fx_maze': '24,1,0,1,0', 'jeje_rays': '50,50,10,0,0.5,255,0,0,255,255,0,0', 'mc_paint_splat': '50,0,255,255,255,255,1', 'mc_australia': '50,0,255,255,255,255,1', 'fx_mineral_mosaic': '1,2,1,100,0', 'samj_Rays_Of_Colors': '300,12,40,16,38,1,0,0,0', 'fx_barnsley_fern': '0,100,30,40,10,178,0,255,1', 'fx_sierpinski': '6,50,0,0,100,100,100,255,255,255,1', 'samj_Motifs_Aleatoires_Symetriques_Degrades': '0,400,4,1,1,1', 'samj_Contours_Gros_Pixels': '1,8,0,20,20,16,1.1,0,0,15,0,0,0,1', 'fx_AbstractFlood': '1,10,7,2,0,10,5,3,255,255,255,255,0,300,10,90,0.7,0,0,0', 'samj_Degrades_XYZ_CIE': '6,800,240,240,40,255,120,40,240,255,0,0,0,100,64,64,0,0,1,0,100,-128,128,-128,128,0,11,0,0', 'samj_EPPE_Transform': '50,50,0,10,10,32,0.1,10,18,0,255,255,255,255,3,0,0.1', 'fx_bwfilmsimulate': '0,0.299,0,0.587,0,0.114,0,1,1,0,0,0,0,0,0,2,0,0,0,16,4,0', 'samj_Lignes_H_ou_V_Colorees': '159,190,195,55,67,140,54,40,39,140,81,88,207,175,190,220,202,196,170,186,192,130,149,139,112,96,96,237,168,138,220,199,205,234,217,219,255,256,256,1,0,0', 'mc_gum_leaf': '50,0,255,255,255,255,1', 'fx_blockism': '3,1.6,0.5,50,0.5,64,0,1,0', 'samj_Marbre': '1,1,8,5,0.2,0,0,0,140,120,220,0,3,1', 'fx_CompositionAnalysis': '0', 'samj_Motif_Plasma': '2,20,20,30,1,75,0', 'fx_shapes': '1,16,10,2,5,90,0,0,1,1,0', 'fx_dodgesketch': '3,10,7,2,0,0', 'mc_maple_leaf': '50,0,255,255,255,255,1', 'samj_Motifs_7200': '2,0,20,20,30,1,75,0,0,255,0,221,255,0,0,0', 'fx_ExposureWeightMap': '0.3,0.3,0.2,0.3,1,0', 'samj_Motifs_7200_VarianteA': '2,0,20,20,30,1,75,0,0,255,0,221,255,0,0,0', 'samj_Steps_V2': '10,10,4,1,10,2,60,0,1.1,10', 'samj_Tissu_Fond_Flou': '0,0,100,100,0,1,0,1,0,0,0,0,0', 'fx_snowflake': '5,1,255,255,255', 'samj_Variation_Stained_Glass': '0,2,8,0,3,40,100,0,1.1,20', 'jeje_periodic_dots': '6,4,0,1,0', 'fx_satin': '20,1,0,0,0,0,255,255,255,255,255,0,0,0,-50,0,0', 'fx_mad_rorscharchp': '3,0,50,1,300,0,0,0,0', 'fx_jobs_colors': '0,0,0', 'fx_StructureTensors': '0.1,0', 'fx_plaid_texture': '50,2,0,90,1,300', 'fx_stars': '10,0,32,5,0.38,0,255,255,100,200', 'samj_en_Contours_Gros_Pixels': '1,8,2,20,20,16,1.1,0,1,15,1,0,0,1', 'fx_dragoncurve': '20,0,1,255,255,255', 'jeje_strip': '45,50,0,1,0', 'samj_Points_Aleatoires_001': '10,255,255,0,255,3,0,1', 'fx_tetris': '10', 'rgb2bayer': '0,1', 'fx_truchet': '32,5,1,1,0', 'fx_camouflage': '9,12,100,30,46,33,75,90,65,179,189,117,255,246,158', 'jeje_turing_pattern': '1,2000,.1,.899,-.91,2,.1,.25', 'fx_polka_dots': '80,20,50,50,0,0.5,0.1,1,255,0,0,255', 'weave': '6,65,0,0.5,0,0,0,0,0', 'texturize_canvas': '20,3,0.6', 'fx_color_ellipses': '400,8,0.1', 'fx_elevation3d': '100,1,1024,1024,0.8,25,0,21,45,0,0,-100,0.5,0.7,2,1', 'fx_steampen': '0.95,14,2,2,0.9,0,1,0,0.5,0.75,0.48,0', 'fx_extrude3d': '10,512,0.6,1024,1024,0.5,57,41,21,45,0,0,-100,0.5,0.7,4,1', 'fx_graphic_boost': '1.25,2,0,0.15,14,0,1,0.5,0.45,2,0,1,0,1,1,0.5,0.45,1,0', 'fx_compose_boostscreen': '0.7,0,0.7', 'fx_imageobject3d': '1,1024,1024,0.5,57,41,21,45,0,0,-100,0.5,0.7,4,1', 'fx_compose_colordoping': '1,0', 'fx_lathing3d': '76,2,361,1024,1024,0.5,0,0,0,45,0,0,-100,0.5,0.7,4,1', 'fx_colorstamp': '1,50,1,20,2,0', 'fx_random3d': '0,50,3,100,45,0,0,-100,0.5,0.7,3,1', 'fx_compose_graphicolor': '0.6,0,0.8', 'fx_compose_comix_color': '1,0,1', 'samj_Adjacent_Annular_Steiner_Chains_en': '50,50,0,0,6,56,20,50,0,255,0,221,127,72,0,255,127,0,145,255,127,0,255,144,127,72,255,0,127,255,217,0,127,255,0,0,127,5,0,0,2,0,0,0,255,0,0,0', 'fx_compose_darkedges': '1,0.5,0,0.7', 'samj_Adjacent_Annular_Steiner_Chains': '50,50,0,0,6,56,20,50,0,255,0,221,127,72,0,255,127,0,145,255,127,0,255,144,127,72,255,0,127,255,217,0,127,255,0,0,127,5,0,0,2,0,0,0,255,0,0,0', 'fx_novelfx': '0,2,6,5,20,0,0.62,14,0,1,0.5,0.78,1.92,0,0,0,1,1,0.5,0.8,1.28,0', 'samj_Rectangles_Adjacents': '10,10,80,80,0,50,6,0,0,0,0,0,255,1,255,255,0,127,0,0,255,127,0,0,0,0,0,0,0,0.5,0.5,1.8,0,0,0,0', 'samj_en_Rectangles_Adjacents': '10,10,80,80,0,50,6,0,0,0,0,0,255,1,255,255,0,127,0,0,255,127,0,0,0,0,0,0,0,0.5,0.5,1.8,0,0,0,0', 'samj_en_Annular_Steiner_Chains': '50,50,50,6,0,0,0,0,255,1,255,255,0,127,64,192,128,127,0,255,0,127,0,0,255,127,0,0,0,0,0,0,0,0.5,0.5,1.8,0,0,0,0', 'samj_Annular_Steiner_Chains': '50,50,50,6,0,0,0,0,255,1,255,255,0,127,64,192,128,127,0,255,0,127,0,0,255,127,0,0,0,0,0,0,0,0.5,0.5,1.8,0,0,0,0', 'fx_compose_heavyscreen': '0.6,0,0.7', 'fx_phoenix': '0.95,14,2,2,0.9,0,0,0,1,1,0', 'fx_smooth_anisotropic': '60,0.16,0.63,0.6,2.35,0.8,30,2,0,1,1,0,1', 'fx_psyglass': '0,20,0.1,1,1,0,1,1,0,1,1,0,0,2,0,0,0', 'fx_viral': '3,0,0,0,0,0', 'fx_compose_vivid_color': '1,0,1', 'fx_compose_vividedges': '1,0.5,0,0.7', 'fx_seamless_turbulence': '15,20,0,1,3,0', 'samj_Noel_2016': '50,50,100,150,7,0,240,45,15,255,-15,2.5,2,0.8,1,1.5,0,0,0,0.25,10,0.8', 'fx_compose_vividscreen': '0.6,0,0.7', 'samj_Chryzodes': '100,0,0,0,255,0,50,50,45,79,3,1,240,128,64,255,0,0,0,0,0,0,0,0,0,0,0', 'fx_m_l_unsharp2': '12,2.18,0.3,1.5,1,0.5,0,0.5,0.8,1.28,0', 'samj_en_Chryzodes': '100,0,0,0,255,0,50,50,45,79,3,1,240,128,64,255,0,0,0,0,0,0,0,0,0,0,0', 'samj_Contour_Line_Laser_LED': '0,1,0', 'samj_dessiner_un_polygone': '5,50,50,0,40,50,1,255,255,0,0,0,0,0,1,0,0,255,0,0,255,0,0,0,127,127,127,0,0,0,0,0,255,255,255,0,0,0,0,1,255,0,0,0,1', 'samj_Egg_Oeuf_Granville': '50,50,0,20,30,10,0,0,0,0,255,1,255,255,0,127,0,0,0,0,0,0,0,0.5,0.5,1.8,0,0,0,0', 'samj_Egg_Oeuf_Hugelschaffer': '50,50,50,6,48,0,0,0,0,0,255,1,255,255,0,127,0,0,0,0,0,0,0,0.5,0.5,1.8,0,0,0,0', 'samj_Egg_Oeuf_Rosillo': '50,50,40,200,300,0,0,0,0,255,1,255,255,0,127,0,0,0,0,0,0,0,0.5,0.5,1.8,0,0,0,0', 'samj_Engrenages_Laser_LED': '80,20,12,14,17,1,1,2,19,250,0,0,0,0', 'fx_equation_parametric': '"sin(t)*(exp(cos(t))-2*cos(4*t)-sin(t/12)^5)","cos(t)*(exp(cos(t))-2*cos(4*t)-sin(t/12)^5)",0,100,4096,1,0,64,0,0,128,0,0,1,1,1', 'fx_compose_darkscreen': '0.7,0,0.7', 'samj_Etoile_De_Pompei_Triangles_Sierpinski': '50,50,30,100,0,0,0,255,0,5,255,0,0,127,255,0,255,127,0,0,255,127,0,255,255,127,255,255,0,127,0,63,255,64,0,0,0,0,0,0,0,0.5,0.5,1.8,0,0,0,0', 'samj_Etoiles_Laser_LED': '1400,5,2,0,0,0,0', 'samj_Etoiles_Remplies_Triangles_Sierpinski': '6,50,50,50,40,30,0,0,0,0,0,255,1,4,255,0,0,127,255,192,64,127,0,0,255,127,0,255,255,127,255,255,0,127,0,0,0,0,0,0,0,0.5,0.5,1.8,0,0,0,0', 'samj_Flocon_De_Neige': '50,50,6,50,40,0,3,192,192,192,1,0,3,255,255,255,0.7,0,0,0,0,0,0,0,0,0.5,0.5,1.8,0,0,0,0', 'samj_Flocon_Laser_LED': '1400,6,5,0', 'samj_Fractal_Tree': '50,100,-90,11,10,20,255,0,0,255,20,0,4,1,0,0.25,10,0.8,0', 'fx_corner_gradient': '255,255,255,128,255,0,0,255,0,255,0,255,0,0,255,255,1', 'fx_custom_gradient': '0,0,0,1,4,1,0,128,100,100,2,0,1,0,"",1,0,0,0,0,255,255,0,0,255,255,255,0,255,255,255,255,255,0,255,255,255,0,255,0,255,0,0,255,255,128,128,128,255,255,0,255,255,0,0,0,0', 'fx_linear_gradient': '0,0,0,255,255,255,255,255,0,45,0,100,0', 'fx_random_gradient': '32,0,0,128,128,128,1', 'fx_ball': '128,0.8,1,1.5,255,0,255', 'samj_Linear_Gradient_CIE_Lab': '0,0,240,40,160,255,240,240,40,255', 'samj_en_Shape_Linear_Gradient_CIE_Lab': '10,10,90,90,2,0,240,40,160,255,240,240,40,255,0,0,0,0,255,0', 'samj_Shape_Linear_Gradient_CIE_Lab': '10,10,90,90,2,0,240,40,160,255,240,240,40,255,0,0,0,0,255,0', 'gtutor_hairlock': '0.5,0.5,0.5,255,255,0,255,0.5,45,0.5,0.5,0', 'Harmonograph_samj_en': '50,50,192,128,64,255,0,0,1000,0,400,150,200,200,100,4,6,2,2,15,270,75,60,0.04,0.04,0.05,0.06,0,0,0,1,1', 'Harmonograph_samj': '50,50,192,128,64,255,0,0,1000,0,400,150,200,200,100,4,6,2,2,15,270,75,60,0.04,0.04,0.05,0.06,0,0,0,1,1', 'samj_Hawaiian_Earring': '50,50,40,6,0,0,0,0,0,255,1,255,255,0,127,0,0,255,127,0,0,0,0,0,0,0,0.5,0.5,1.8,0,0,0,0', 'samj_en_Hawaiian_Earring': '50,50,40,6,0,0,0,0,0,255,1,255,255,0,127,0,0,255,127,0,0,0,0,0,0,0,0.5,0.5,1.8,0,0,0,0', 'Traits_Strokes_samj_en': '50,50,35,0,100,0,30,0,360,240,60,120,255,0,0,0,20,0,0,0,1,1', 'fx_coloredobject3d': '1,128,128,128,255,0.5,0.5,0.5,57,41,21,45,0,0,-100,0.5,0.7,4,1', 'samj_en_Lignes_Epaisseur_Variable': '0,32,3,0,0,0,255,255,255,255,255,0,0,1,0,0,0,0,0,0,0.5,0.5,1.8,0,0', 'fx_lissajous': '4096,0.9,0.9,3,8,7,0,0,0,0,0,0,0,0,255,255,255,255', 'samj_Orbites': '100,0,0,0,255,50,50,20,79,45,2,240,128,64,255,0,0,0,0,0,0,0,0', 'samj_Cercles_Tangents_Dans_Cercle': '50,50,50,40,0,0,0,0,255,1,127,127,127,127,255,0,0,127,0,255,0,127,0,0,255,127,255,0,255,127,255,255,0,127,0,255,255,127,192,128,64,127,64,192,128,127,128,64,192,127,192,64,128,127,0,0,0,0,0,0,0,0.5,0.5,1.8,0,0,0,0', 'samj_en_Cercles_Tangents_Dans_Cercle': '50,50,50,40,0,0,0,0,255,1,127,127,127,127,255,0,0,127,0,255,0,127,0,0,255,127,255,0,255,127,255,255,0,127,0,255,255,127,192,128,64,127,64,192,128,127,128,64,192,127,192,64,128,127,0,0,0,0,0,0,0,0.5,0.5,1.8,0,0,0,0', 'Pintograph_samj': '50,50,192,128,64,255,0,0,1000,0,400,150,200,200,100,4.00,4.05,4.16,4.32,75,150,75,60,0,0,0,1,1', 'Pintograph_samj_en': '50,50,192,128,64,255,0,0,1000,0,400,150,200,200,100,4.00,4.05,4.16,4.32,75,150,75,60,0,0,0,1,1', 'fx_plasma': '0.5,0,8,0,0,128,128,128', 'fx_equation_plot': '"X*c+10*cos(X+c+u)",-10,10,100,3,2,0', 'samj_Arbre_Pythagore': '50,95,11,12,255,0,0,255,20,"A",1,0,0,0.25,10,0.8,0', 'fx_rainbow': '80,80,175,175,3,80', 'samj_Rosace_Triangles_Sierpinski': '6,6,50,50,50,-15,25,5,30,0,0,0,255,0,0,0,0,3,0,0,255,127,255,255,0,127,128,64,192,127,64,128,192,127,0,255,255,127,0,0,0,0,0,0,0,0,0.5,0.5,1.8,0,0,0,0', 'samj_en_Linear_Gradient_CIE_Lab': '0,0,240,40,160,255,240,240,40,255', 'fx_shadebobs': '50,5,200,1,-1,2,1,0.8,0,8', 'samj_en_Cercles_Qui_Tournent': '800,255,255,255,255,0,1,0.5,0.33,7,17,1,0.5,0.33,7,17,1,10,0,0,0,255,0,0,0,0,0,0,0,0.5,0.5,1.8,0', 'samj_Formes_Geometriques_Simples': '50,50,127,127,127,127,255,255,0,255,0,0,255,255,5,40,40,4,0,0,1', 'samj_Lignes_Epaisseur_Variable': '0,32,3,0,0,0,255,255,255,255,255,0,0,1,0,0,0,0,0,0,0.5,0.5,1.8,0,0', 'fx_superformula': '4096,0.9,0.9,8,1,5,8,0,0,0,3,128,255,128,255', 'samj_Cercles_Qui_Tournent': '800,255,255,255,255,0,1,0.5,0.33,7,17,1,0.5,0.33,7,17,1,10,0,0,0,255,0,0,0,0,0,0,0,0.5,0.5,1.8,0', 'samj_en_Formes_Geometriques_Simples': '50,50,127,127,127,127,255,255,0,255,0,0,255,255,5,40,40,4,0,0,1', 'samj_Poisson_D_Avril': '50,50,40,2,0,0,0,0,255,1,250,60,10,255,255,255,255,255,0,0,0,0,0,0,0,0.5,0.5,1.8,0,0,0,0', 'banding_denoise': '5,5,5,10,0', 'samj_Superposition_Triangles_Sierpinski': '6,6,50,50,50,1,20,30,0,0,0,255,1,4,0,0,255,127,255,255,0,127,128,64,192,127,64,128,192,127,0,255,255,127,0,0,0,0,0,0,0,0,0.5,0.5,1.8,0,0,0,0', 'samj_en_Flocon_De_Neige': '50,50,6,50,40,0,3,192,192,192,1,0,3,255,255,255,0.7,0,0,0,0,0,0,0,0,0.5,0.5,1.8,0,0,0,0', 'samj_Chains_Solidify': '50,50,0,6,56,20,50,0,255,0,221,255,72,0,255,255,0,145,255,255,0,255,144,255,72,255,0,255,255,217,0,255,255,0,0,255,5,255,127,0,255,0,0,0,255,100', 'bayer2rgb': '6,6,4', 'Traits_Strokes_samj': '50,50,35,0,100,0,30,0,360,240,60,120,255,0,0,0,20,0,0,0,1,1', 'samj_Palette_De_Degrades': '159,190,195,55,67,140,54,40,39,140,81,88,207,175,190,220,202,196,170,186,192,130,149,139,112,96,96,237,168,138,220,199,205,234,217,219,0,0,256,2', 'Spirographe_samj_en': '50,50,200,50,150,192,128,64,255,0,0,3,0,1,0,0,0,255,0,0,255,0,255,255,0,255,0,0,0,1,1', 'fx_tree': '11,10000,0,0,15,150,0,2.15,0.8,-40,40,10,75,0,70,20,40,25,0,255,100,70,140,60,255,100,0.4,0.4', 'afre_cleantext': '8,1,80,95', 'gcd_deinterlace2x': '40,0,0,2,0,1', 'Spirographe_samj': '50,50,200,50,150,192,128,64,255,0,0,3,0,1,0,0,0,255,0,0,255,0,255,255,0,255,0,0,0,1,1', 'samj_Splines_Test': '50,50,30,30,90,30,1,10,2,2,2,2,2,2,2,2,255,255,0,255,0,255,255,255,1,0,0', 'Triangles_Shades_Adjacents': '0,50,50,60,-1,0,255,255,255,255,0,221,72,0,255,0,145,255,0,255,144,72,255,0,255,217,0,255,0,0,5,0,0,128,128,128,1,0,3,1,0', 'fx_pahlsson_descreen': '0', 'samj_Des_Lignes_002': '100,0,0,192,128,64,255,0,0,1,50,50,0,0,0,0,1', 'samj_Test_Visu_3D': '1,"C:\\GimpEval-2.9.5-Win\\images_test\\GMIC\\cube.off",0.5,1,1,0,0,0,1,0,0,0,1024,1024,0.5,0,0,0,45,0,0,-100,0.5,0.7,2,1,400,1,225,255,255,255', 'fx_turbulence': '128,6,4,0,0', 'gcd_despeckle': '20,10', 'samj_en_Des_Lignes_002': '100,0,0,192,128,64,255,0,0,1,50,50,0,0,0,0,1', 'iain_fast_denoise_p': '0,0,1,0,0,0,1', 'Twisted_Rays_en': '800,1,0.2,2,5,21,0,0,0,0,255,255,0,255,255,255,0,255,0,255,255,255,0,255,255,0,0,255,255,0,255,255,255,255,255,255,0,0,0,0,255,0,2,2,0,0,5,0,0', 'iain_recursive_median_p': '3,1,0,0,1', 'fx_inpaint_holes': '4,20,1', 'iain_nr_2019': '1,0,0,0,0.5,1,0,5,3,0,3,0,.5,4,0', 'Twisted_Rays': '800,1,0.2,2,5,21,0,0,0,0,255,255,0,255,255,255,0,255,0,255,255,255,0,255,255,0,0,255,255,0,255,255,255,255,255,255,0,0,0,0,255,0,2,2,0,0,5,0,0', 'fx_inpaint_morpho': '255,0,0,255,0', 'jeje_scandoc': '3,1,90,5,0', 'rep_binary_quaddro_mc_gui': '0,0,0,0,1,2,0,1,2,3,0,1,2,3,4,0,8,8,128,2,0,0,0,1,0,8,8,128,2,0,0,0,1,0,8,8,128,2,0,0,0,1,0,8,8,128,2,0,0,0,1,0,8,8,128,2,0,0,0,1', 'jeje_local_wiener': '2,11,0,0', 'fx_inpaint_matchpatch': '0,9,10,5,1,255,0,0,255,0,0', 'samj_CorLine': '0,10,0.5,0,0,50,1,0', 'gui_rep_shape_brick': '150,150,5,5,0,0,0,0,0,0,170,0,0,255,85,0,0,255,121,77,2,255,0,41,100,0', 'jeje_unstrip': '1,20,4,1,0,0', 'rep_color_existence_distribution_rgb8': '1', 'samj_CorLine_B': '0,1,10,0,0,0,0.5,0,0,50,1,0', 'fx_inpaint_patch': '7,16,0.1,1.2,0,0.05,10,1,255,0,0,255,0,"100%"', 'jeje_denoise_patch_dict': '1,8,1.1,1.1,0,0', 'fx_inpaint_pde': '75,1,20,255,0,0,255,0', 'goof_res': '8,0,0,0', 'fx_scale_dcci2x': '1.15,5,0', 'jeje_denoise_iuwt': '3,4,2,0', 'fx_upscale_smart': '"200%","200%",2,0.4,50', 'fx_rep_nebulous': '0,4,10,10,0,0,0,1,0,0,1,0,0,0,0,2,0,1,3', 'iain_pixel_denoise_p': '2,1,11,0,1', 'sp': 'cliff', 'fx_scalenx': '0,0', 'rep_mj_newf': '16,0,0,128,9,0,75,5,10,50,50,45,0,0,0', 'plasma_transition': '0.5,5,1,42', 'fx_modulo': '1,0', 'fx_faded_mirror': '0,10,10', 'randomwaves': '84,80.,1.2,42', 'gui_rep_prime_surface': '0,0', 'fx_rep_rand_sqrrecfill': '0,0,15,2,1,1,0,1,1,1,0,0,0', 'gaap_test': '0,0,0,0', 'fx_adjust_orientation': '5', 'rep_binary_quaddro_basic_gui': '0,0,8,8,128,2,0,0,0,256,255,1,361,361', 'fx_gca': '255,255,255,1,0,0,0', 'fx_grain': '40,5,0,2,0.8,0.5,0.5,1,0,0.5,0.6,0.2,0.5,0', 'fx_apply_curve': '0,-1,128,-1,128,-1,128,-1,128,-1,128,255,1,0,0,0,0', 'fx_perspective_scale': '2,75,0,0,0', 'fx_lavalampbw': '3,30,1,20,2,0.01,0', 'gui_rep_tfrac': '0,0,10000,255,3,0,0,1,1,1,1,0,0,0,"atan2(a^2","b/sin(a)","sin(a)/cos(b)","b/cos(a)","a/sin(b)","b/cos(a+b)","a","b","a","b",0,3,0', 'KittyRings': '30,8,0,1,113,0,113,0,255,0', 'dt_segment_shaded': '1,0.7,1', 'fx_moire': '1,0,2,1,1,2,1,5', 'gui_layer_info': '1', 'fx_tk_make3D': '0,20,0,20,0,0,0,0,0,0,0,0,0,1.2,25,1,0,1,0,0,0,2,200', 'moon2panorama': '0,0,0,360,0,0,1,0,0', 'fx_text_pointcloud3d': '64,"G\'MIC","Rocks!",1,200,220,255,255,255,255,255,2,2,1,19', 'fx_tk_animateobject': '0,0,0,0.5,0.5,400,2,0,0,0,0,0,1,0,0,1', 'fx_tk_deana': '20,2', 'fx_souphead_filter': '0', 'fx_tk_depthmap': '0,20,0,0,0,0,0,0,0,0', 'fx_transition3d': '10,8,8,1,1,0,800,1', 'fx_tk_lenticular': '30,0,5,0,1,0', 'disco': '10,15,20,250', 'gcd_unstereo': '5,0.1,1,1,1,1,0', 'spiral_RGB': '1,3,5,0', 'fx_tk_retouch': '30,3,1,20,1.5,1,2.5,0,0,0', 'fx_tk_depth_obtain': '0,0.1,100,0', 'samj_CeKoaSa_001': '0,15,3,1,3,0', 'gcd_stereo_img': '0,0.5,1.2,1,0.25,2,4,1,0', 'mc_flou': '30,6,1,1,1,0,255,1,1,1,0', 'fx_tk_dof': '50,50,30,60,5,15,2,0,0,200,40,2,0,0,0,0,0.01,0,1,0,0', 'samj_CeKoaSa_002': '0,15,3,1,3,1,0', 'samj_CeKoaSa_003': '0,5,1,1,3,0', 'fx_tk_stereoimage': '0,0,1,0,1,0', 'mc_pendraw': '8,0.8,450,21,0.5,1,0,0,255,0,0', 'fx_tk_infrared': '0.75,0.5,-100,0.75,0,1,0,0,1,1,0,50,0', 'samj_CeKoaSa_005': '16,16,0,0,0.2,1,1,0,1,0', 'samj_BoxFiter_Map': '2,3,3,0,0,0,2,127,16,0,0,0.2', 'samj_BoxFiter_Test': '2,3,3,1,2', 'samj_CeKoaSa_004': '30,0,0,0.8,0,0', 'samj_CeKoaSa_007': '8,8,10,8,8', 'Polygonize_GUI': '300,10,10,10,10,0,0', 'samj_CeKoaSa_008': '64,64,4,1,2,16,1,20,0.1,0,1,64,1,2,10,0.8,255,255,255,255,0', 'samj_CeKoaSa_010': '30,10,0.1,2,10', 'samj_Relief_A': '3,1,0,1,16,1,50,1,1.0,1.2,1,1,1,1,1,1,0,0,0,0,0,0,100', 'samj_CeKoaSa_011': '0.2,0,0,5,0,0,0,0,240,40,160,255,240,240,40,255,0,50,205', 'samj_test_B': '100', 'samj_test_C': '100', 'samj_test_E': '0,0.7,0.3,0.6,1.1,0,200,125,50,0,1', 'samj_test_D': '40,255,10,30,5,0,8,0,4,0,25', 'samj_test_F': '40,50,1', 'samj_test_G': '0,0,0,30', 'fx_image_sample': '0,0,0', 'samj_Test_Solidify': '10,10,1,0.02,8,1,75,0,20', 'samj_test_x_color_curves': '1,0', 'samj_gimp_texture_zero_zero_deux': '0,10,4,10,0.5,1,1,1,0.3', 'samj_Texture_Aquarelle_1': '10,10,4,3,251,237,206,1', 'demo_xy': '1,1', 'samj_Toile_D_Araignee': '0,10,4', 'demo_ra': '1,1', 'mathmap_flag': '0.05,5,1,5', 'mathmap_spiral': '5,0'}


def gmic_enum_items_cb0(self, context):
    l = (('fx_rorschach', 'fx_rorschach', 'fx_rorschach'), ('fx_camouflage', 'fx_camouflage', 'fx_camouflage')) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb0.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator0(bpy.types.Operator):
    bl_idname = "object.gmic_operator0"
    bl_label = "パターン"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb0)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb0.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb1(self, context):
    l = (('fx_emulate_film_instant_pro', 'fx_emulate_film_instant_pro', 'fx_emulate_film_instant_pro'), ('fx_emulate_film_instant_consumer', 'fx_emulate_film_instant_consumer', 'fx_emulate_film_instant_consumer'), ('fx_emulate_film_negative_color', 'fx_emulate_film_negative_color', 'fx_emulate_film_negative_color')) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb1.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator1(bpy.types.Operator):
    bl_idname = "object.gmic_operator1"
    bl_label = "フィルムエミュレーション"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb1)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb1.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb2(self, context):
    l = (('fx_frame_blur', 'fx_frame_blur', 'fx_frame_blur'),) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb2.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator2(bpy.types.Operator):
    bl_idname = "object.gmic_operator2"
    bl_label = "フレーム"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb2)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb2.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb3(self, context):
    l = (('fx_scalenx', 'fx_scalenx', 'fx_scalenx'), ('deinterlace', 'deinterlace', 'deinterlace'), ('fx_remove_hotpixels', 'fx_remove_hotpixels', 'fx_remove_hotpixels'), ('fx_inpaint_patch', 'fx_inpaint_patch', 'fx_inpaint_patch'), ('fx_inpaint_matchpatch', 'fx_inpaint_matchpatch', 'fx_inpaint_matchpatch'), ('fx_solidify_td', 'fx_solidify_td', 'fx_solidify_td'), ('iain_fast_denoise_p', 'iain_fast_denoise_p', 'iain_fast_denoise_p')) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb3.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator3(bpy.types.Operator):
    bl_idname = "object.gmic_operator3"
    bl_label = "修復"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb3)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb3.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb4(self, context):
    l = (('fx_light_leaks', 'fx_light_leaks', 'fx_light_leaks'),) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb4.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator4(bpy.types.Operator):
    bl_idname = "object.gmic_operator4"
    bl_label = "光と影"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb4)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb4.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb5(self, context):
    l = (('fx_gaussian_blur', 'fx_gaussian_blur', 'fx_gaussian_blur'), ('fx_glow', 'fx_glow', 'fx_glow'), ('fx_blur_angular', 'fx_blur_angular', 'fx_blur_angular'), ('fx_blur_radial', 'fx_blur_radial', 'fx_blur_radial'), ('fx_blur_linear', 'fx_blur_linear', 'fx_blur_linear'), ('fx_blur_dof', 'fx_blur_dof', 'fx_blur_dof'), ('fx_chromatic_aberrations', 'fx_chromatic_aberrations', 'fx_chromatic_aberrations'), ('fx_lomo', 'fx_lomo', 'fx_lomo')) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb5.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator5(bpy.types.Operator):
    bl_idname = "object.gmic_operator5"
    bl_label = "劣化"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb5)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb5.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb6(self, context):
    l = (('fx_distort_lens', 'fx_distort_lens', 'fx_distort_lens'), ('fx_equirectangular2nadirzenith', 'fx_equirectangular2nadirzenith', 'fx_equirectangular2nadirzenith')) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb6.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator6(bpy.types.Operator):
    bl_idname = "object.gmic_operator6"
    bl_label = "変形"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb6)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb6.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb7(self, context):
    l = (('fx_cupid', 'fx_cupid', 'fx_cupid'), ('fx_corner_gradient', 'fx_corner_gradient', 'fx_corner_gradient'), ('fx_sierpinski', 'fx_sierpinski', 'fx_sierpinski'), ('fx_heart', 'fx_heart', 'fx_heart'), ('fx_barnsley_fern', 'fx_barnsley_fern', 'fx_barnsley_fern'), ('fx_ball', 'fx_ball', 'fx_ball'), ('fx_equation_parametric', 'fx_equation_parametric', 'fx_equation_parametric'), ('fx_rainbow', 'fx_rainbow', 'fx_rainbow'), ('fx_snowflake', 'fx_snowflake', 'fx_snowflake'), ('fx_extrude3d', 'fx_extrude3d', 'fx_extrude3d')) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb7.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator7(bpy.types.Operator):
    bl_idname = "object.gmic_operator7"
    bl_label = "描画"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb7)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb7.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb8(self, context):
    l = (('fx_colorize_interactive', 'fx_colorize_interactive', 'fx_colorize_interactive'), ('fx_colorize_comics', 'fx_colorize_comics', 'fx_colorize_comics'), ('fx_autofill_lineart', 'fx_autofill_lineart', 'fx_autofill_lineart')) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb8.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator8(bpy.types.Operator):
    bl_idname = "object.gmic_operator8"
    bl_label = "白黒画像編集"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb8)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb8.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb9(self, context):
    l = (('fx_sepia', 'fx_sepia', 'fx_sepia'), ('fx_transfer_colors', 'fx_transfer_colors', 'fx_transfer_colors'), ('fx_select_color', 'fx_select_color', 'fx_select_color'), ('fx_selective_desaturation', 'fx_selective_desaturation', 'fx_selective_desaturation')) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb9.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator9(bpy.types.Operator):
    bl_idname = "object.gmic_operator9"
    bl_label = "色"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb9)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb9.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb10(self, context):
    l = (('fx_quadtree', 'fx_quadtree', 'fx_quadtree'),) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb10.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator10(bpy.types.Operator):
    bl_idname = "object.gmic_operator10"
    bl_label = "芸術的"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb10)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb10.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb11(self, context):
    l = (('fx_sharpen_texture', 'fx_sharpen_texture', 'fx_sharpen_texture'), ('jeje_dehaze', 'jeje_dehaze', 'jeje_dehaze')) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb11.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator11(bpy.types.Operator):
    bl_idname = "object.gmic_operator11"
    bl_label = "詳細"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb11)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb11.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb12(self, context):
    l = (('fx_extract_foreground', 'fx_extract_foreground', 'fx_extract_foreground'),) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb12.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator12(bpy.types.Operator):
    bl_idname = "object.gmic_operator12"
    bl_label = "輪郭"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb12)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb12.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb13(self, context):
    l = (('fx_frame_seamless', 'fx_frame_seamless', 'fx_frame_seamless'),) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb13.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator13(bpy.types.Operator):
    bl_idname = "object.gmic_operator13"
    bl_label = "配列とタイリング"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb13)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb13.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb14(self, context):
    l = (('_none_', '_none_', '_none_'), ('_none_', '_none_', '_none_'), ('_none_', '_none_', '_none_'), ('_none_', '_none_', '_none_'), ('gui_download_all_data', 'gui_download_all_data', 'gui_download_all_data'), ('_none_', '_none_', '_none_'), ('_none_', '_none_', '_none_'), ('_none_', '_none_', '_none_'), ('fx_gmicky', 'fx_gmicky', 'fx_gmicky'), ('_none_', '_none_', '_none_'), ('_none_', '_none_', '_none_')) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb14.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator14(bpy.types.Operator):
    bl_idname = "object.gmic_operator14"
    bl_label = "About"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb14)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb14.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb15(self, context):
    l = (('afre_contrastfft', 'afre_contrastfft', 'afre_contrastfft'), ('afre_edge', 'afre_edge', 'afre_edge'), ('fx_gamify', 'fx_gamify', 'fx_gamify'), ('afre_gleam', 'afre_gleam', 'afre_gleam'), ('afre_halfhalf', 'afre_halfhalf', 'afre_halfhalf'), ('fx_hnorm', 'fx_hnorm', 'fx_hnorm'), ('afre_sharpenfft', 'afre_sharpenfft', 'afre_sharpenfft'), ('afre_softlight', 'afre_softlight', 'afre_softlight'), ('afre_vigcirc', 'afre_vigcirc', 'afre_vigcirc'), ('afre_vigrect', 'afre_vigrect', 'afre_vigrect')) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb15.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator15(bpy.types.Operator):
    bl_idname = "object.gmic_operator15"
    bl_label = "afre"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb15)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb15.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb16(self, context):
    l = (('mc_dragonfly', 'mc_dragonfly', 'mc_dragonfly'), ('mc_kookaburra', 'mc_kookaburra', 'mc_kookaburra'), ('mc_paw', 'mc_paw', 'mc_paw'), ('mc_rooster', 'mc_rooster', 'mc_rooster')) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb16.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator16(bpy.types.Operator):
    bl_idname = "object.gmic_operator16"
    bl_label = "Animals"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb16)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb16.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb17(self, context):
    l = (('Annular_Steiner_Chain_Round_Tile_en', 'Annular_Steiner_Chain_Round_Tile_en', 'Annular_Steiner_Chain_Round_Tile_en'), ('Annular_Steiner_Chain_Round_Tile', 'Annular_Steiner_Chain_Round_Tile', 'Annular_Steiner_Chain_Round_Tile'), ('fx_array_fade', 'fx_array_fade', 'fx_array_fade'), ('fx_array_mirror', 'fx_array_mirror', 'fx_array_mirror'), ('fx_array_color', 'fx_array_color', 'fx_array_color'), ('array_random', 'array_random', 'array_random'), ('fx_array', 'fx_array', 'fx_array'), ('fx_asciiart', 'fx_asciiart', 'fx_asciiart'), ('Cercles_Concentriques_A', 'Cercles_Concentriques_A', 'Cercles_Concentriques_A'), ('fx_chessboard', 'fx_chessboard', 'fx_chessboard'), ('samj_Scintillements_Colores_en', 'samj_Scintillements_Colores_en', 'samj_Scintillements_Colores_en'), ('Cercles_Concentriques_A_en', 'Cercles_Concentriques_A_en', 'Cercles_Concentriques_A_en'), ('fx_dices', 'fx_dices', 'fx_dices'), ('fx_drawn_montage', 'fx_drawn_montage', 'fx_drawn_montage'), ('fx_extract_objects', 'fx_extract_objects', 'fx_extract_objects'), ('fx_imagegrid', 'fx_imagegrid', 'fx_imagegrid'), ('fx_imagegrid_hexagonal', 'fx_imagegrid_hexagonal', 'fx_imagegrid_hexagonal'), ('fx_imagegrid_triangular', 'fx_imagegrid_triangular', 'fx_imagegrid_triangular'), ('samj_en_Coeurs_Hearts_002', 'samj_en_Coeurs_Hearts_002', 'samj_en_Coeurs_Hearts_002'), ('fx_make_seamless', 'fx_make_seamless', 'fx_make_seamless'), ('fx_frame_seamless', 'fx_frame_seamless', 'fx_frame_seamless'), ('fx_ministeck', 'fx_ministeck', 'fx_ministeck'), ('fx_montage', 'fx_montage', 'fx_montage'), ('fx_puzzle', 'fx_puzzle', 'fx_puzzle'), ('samj_reptile_en', 'samj_reptile_en', 'samj_reptile_en'), ('samj_Bulles_Colorees', 'samj_Bulles_Colorees', 'samj_Bulles_Colorees'), ('samj_Carres_Noirs', 'samj_Carres_Noirs', 'samj_Carres_Noirs'), ('samj_Coeurs_Hearts_002', 'samj_Coeurs_Hearts_002', 'samj_Coeurs_Hearts_002'), ('samj_Ellipses_Colorees', 'samj_Ellipses_Colorees', 'samj_Ellipses_Colorees'), ('samj_Losanges_Colores', 'samj_Losanges_Colores', 'samj_Losanges_Colores'), ('samj_Moirage_Spline', 'samj_Moirage_Spline', 'samj_Moirage_Spline'), ('samj_Moirage_Spline_XY', 'samj_Moirage_Spline_XY', 'samj_Moirage_Spline_XY'), ('samj_Pixelisation_Contours', 'samj_Pixelisation_Contours', 'samj_Pixelisation_Contours'), ('samj_Pointes_De_Diamants_Colorees', 'samj_Pointes_De_Diamants_Colorees', 'samj_Pointes_De_Diamants_Colorees'), ('samj_reptile', 'samj_reptile', 'samj_reptile'), ('samj_Scintillements_Colores', 'samj_Scintillements_Colores', 'samj_Scintillements_Colores'), ('fx_taquin', 'fx_taquin', 'fx_taquin'), ('fx_rotate_tileable', 'fx_rotate_tileable', 'fx_rotate_tileable'), ('fx_isolate_tiles', 'fx_isolate_tiles', 'fx_isolate_tiles'), ('fx_normalize_tiles', 'fx_normalize_tiles', 'fx_normalize_tiles'), ('fx_parameterize_tiles', 'fx_parameterize_tiles', 'fx_parameterize_tiles'), ('fx_shift_tiles', 'fx_shift_tiles', 'fx_shift_tiles'), ('fx_rotate_tiles', 'fx_rotate_tiles', 'fx_rotate_tiles')) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb17.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator17(bpy.types.Operator):
    bl_idname = "object.gmic_operator17"
    bl_label = "Arrays & Tiles"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb17)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb17.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb18(self, context):
    l = (('samj_Angoisse_en', 'samj_Angoisse_en', 'samj_Angoisse_en'), ('gcd_aurora', 'gcd_aurora', 'gcd_aurora'), ('fx_crayongraffiti2', 'fx_crayongraffiti2', 'fx_crayongraffiti2'), ('fx_bokeh', 'fx_bokeh', 'fx_bokeh'), ('fx_brushify', 'fx_brushify', 'fx_brushify'), ('cartoon', 'cartoon', 'cartoon'), ('samj_en_chalkitup', 'samj_en_chalkitup', 'samj_en_chalkitup'), ('samj_chalkitup', 'samj_chalkitup', 'samj_chalkitup'), ('fx_charred_plastic', 'fx_charred_plastic', 'fx_charred_plastic'), ('fx_circle_abstraction', 'fx_circle_abstraction', 'fx_circle_abstraction'), ('fx_ColorAbstractionPaint', 'fx_ColorAbstractionPaint', 'fx_ColorAbstractionPaint'), ('Engrave_colore_en', 'Engrave_colore_en', 'Engrave_colore_en'), ('fx_cpencil', 'fx_cpencil', 'fx_cpencil'), ('samj_Contour_Drawings_en', 'samj_Contour_Drawings_en', 'samj_Contour_Drawings_en'), ('fx_cubism', 'fx_cubism', 'fx_cubism'), ('fx_cutout', 'fx_cutout', 'fx_cutout'), ('fx_diffusiontensors', 'fx_diffusiontensors', 'fx_diffusiontensors'), ('fx_dreamsmooth', 'fx_dreamsmooth', 'fx_dreamsmooth'), ('fx_dreamy_abstraction', 'fx_dreamy_abstraction', 'fx_dreamy_abstraction'), ('fx_dreamy_watercolour', 'fx_dreamy_watercolour', 'fx_dreamy_watercolour'), ('samj_Edges_And_LIC', 'samj_Edges_And_LIC', 'samj_Edges_And_LIC'), ('fx_ellipsionism', 'fx_ellipsionism', 'fx_ellipsionism'), ('fx_feltpen', 'fx_feltpen', 'fx_feltpen'), ('gtutor_fpaint', 'gtutor_fpaint', 'gtutor_fpaint'), ('samj_Flamboyance_Test', 'samj_Flamboyance_Test', 'samj_Flamboyance_Test'), ('fractalize', 'fractalize', 'fractalize'), ('samj_en_Texture_Granuleuse', 'samj_en_Texture_Granuleuse', 'samj_en_Texture_Granuleuse'), ('samj_Texture_Granuleuse', 'samj_Texture_Granuleuse', 'samj_Texture_Granuleuse'), ('fx_graphic_boost4', 'fx_graphic_boost4', 'fx_graphic_boost4'), ('fx_graphic_novelfxl', 'fx_graphic_novelfxl', 'fx_graphic_novelfxl'), ('fx_hard_painting', 'fx_hard_painting', 'fx_hard_painting'), ('fx_hardsketchbw', 'fx_hardsketchbw', 'fx_hardsketchbw'), ('fx_highlight_bloom', 'fx_highlight_bloom', 'fx_highlight_bloom'), ('fx_poster_hope', 'fx_poster_hope', 'fx_poster_hope'), ('fx_houghsketchbw', 'fx_houghsketchbw', 'fx_houghsketchbw'), ('fx_illustration_look', 'fx_illustration_look', 'fx_illustration_look'), ('fx_kuwahara', 'fx_kuwahara', 'fx_kuwahara'), ('fx_linify', 'fx_linify', 'fx_linify'), ('fx_lylejk_painting', 'fx_lylejk_painting', 'fx_lylejk_painting'), ('fx_Squiggly', 'fx_Squiggly', 'fx_Squiggly'), ('fx_MorphoPaint', 'fx_MorphoPaint', 'fx_MorphoPaint'), ('fx_neon', 'fx_neon', 'fx_neon'), ('fx_neon_alpha', 'fx_neon_alpha', 'fx_neon_alpha'), ('fx_otsu_hessian_blend', 'fx_otsu_hessian_blend', 'fx_otsu_hessian_blend'), ('samj_Barbouillage_Paint_Daub_en', 'samj_Barbouillage_Paint_Daub_en', 'samj_Barbouillage_Paint_Daub_en'), ('fx_painting', 'fx_painting', 'fx_painting'), ('fx_pastell', 'fx_pastell', 'fx_pastell'), ('fx_pen_drawing', 'fx_pen_drawing', 'fx_pen_drawing'), ('fx_tk_photoillustration', 'fx_tk_photoillustration', 'fx_tk_photoillustration'), ('samj_Plasmic', 'samj_Plasmic', 'samj_Plasmic'), ('samj_Plasmic_V2', 'samj_Plasmic_V2', 'samj_Plasmic_V2'), ('fx_polygonize_delaunay', 'fx_polygonize_delaunay', 'fx_polygonize_delaunay'), ('fx_polygonize', 'fx_polygonize', 'fx_polygonize'), ('fx_poster_edges', 'fx_poster_edges', 'fx_poster_edges'), ('fx_posterize', 'fx_posterize', 'fx_posterize'), ('fx_pdithered', 'fx_pdithered', 'fx_pdithered'), ('fx_quadtree', 'fx_quadtree', 'fx_quadtree'), ('fx_rodilius', 'fx_rodilius', 'fx_rodilius'), ('samj_Angoisse', 'samj_Angoisse', 'samj_Angoisse'), ('samj_Barbouillage_Paint_Daub', 'samj_Barbouillage_Paint_Daub', 'samj_Barbouillage_Paint_Daub'), ('samj_Color_EdgesO_Engrave', 'samj_Color_EdgesO_Engrave', 'samj_Color_EdgesO_Engrave'), ('samj_Contour_Epais', 'samj_Contour_Epais', 'samj_Contour_Epais'), ('samj_Couleurs_Rayees', 'samj_Couleurs_Rayees', 'samj_Couleurs_Rayees'), ('samj_Couleurs_Rayees_2', 'samj_Couleurs_Rayees_2', 'samj_Couleurs_Rayees_2'), ('samj_Diff_Tensors_Blend', 'samj_Diff_Tensors_Blend', 'samj_Diff_Tensors_Blend'), ('samj_fond_broderie', 'samj_fond_broderie', 'samj_fond_broderie'), ('samj_Fond_Brosse', 'samj_Fond_Brosse', 'samj_Fond_Brosse'), ('samj_fx_sketchbw_modifie', 'samj_fx_sketchbw_modifie', 'samj_fx_sketchbw_modifie'), ('samj_Gris_Raye', 'samj_Gris_Raye', 'samj_Gris_Raye'), ('samj_Impressions', 'samj_Impressions', 'samj_Impressions'), ('samj_Isophotes_Vers_Aquarelle', 'samj_Isophotes_Vers_Aquarelle', 'samj_Isophotes_Vers_Aquarelle'), ('samj_Pointillisme', 'samj_Pointillisme', 'samj_Pointillisme'), ('samj_Pointillisme_B', 'samj_Pointillisme_B', 'samj_Pointillisme_B'), ('samj_TensorTest', 'samj_TensorTest', 'samj_TensorTest'), ('samj_texture_coloree', 'samj_texture_coloree', 'samj_texture_coloree'), ('fx_shapeism', 'fx_shapeism', 'fx_shapeism'), ('fx_sharp_abstract', 'fx_sharp_abstract', 'fx_sharp_abstract'), ('fx_SimpleNoiseCanvas', 'fx_SimpleNoiseCanvas', 'fx_SimpleNoiseCanvas'), ('samj_Test_Skeletik', 'samj_Test_Skeletik', 'samj_Test_Skeletik'), ('fx_sketchbw', 'fx_sketchbw', 'fx_sketchbw'), ('fx_smooth_abstract', 'fx_smooth_abstract', 'fx_smooth_abstract'), ('fx_stylize', 'fx_stylize', 'fx_stylize'), ('samj_texture_coloree_en', 'samj_texture_coloree_en', 'samj_texture_coloree_en'), ('fx_vector_painting', 'fx_vector_painting', 'fx_vector_painting'), ('warhol', 'warhol', 'warhol'), ('fx_watercolor', 'fx_watercolor', 'fx_watercolor'), ('fx_draw_whirl', 'fx_draw_whirl', 'fx_draw_whirl'), ('fx_whirling_lines', 'fx_whirling_lines', 'fx_whirling_lines')) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb18.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator18(bpy.types.Operator):
    bl_idname = "object.gmic_operator18"
    bl_label = "Artistic"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb18)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb18.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb19(self, context):
    l = (('fx_stencilbw', 'fx_stencilbw', 'fx_stencilbw'), ('fx_blackandwhite', 'fx_blackandwhite', 'fx_blackandwhite'), ('fx_charcoal', 'fx_charcoal', 'fx_charcoal'), ('fx_colorize_interactive', 'fx_colorize_interactive', 'fx_colorize_interactive'), ('fx_recolorize', 'fx_recolorize', 'fx_recolorize'), ('fx_bwrecolorize', 'fx_bwrecolorize', 'fx_bwrecolorize'), ('fx_autofill_lineart', 'fx_autofill_lineart', 'fx_autofill_lineart'), ('fx_colorize_lineart', 'fx_colorize_lineart', 'fx_colorize_lineart'), ('fx_colorize_lineart_smart', 'fx_colorize_lineart_smart', 'fx_colorize_lineart_smart'), ('fx_gcd_norm_eq', 'fx_gcd_norm_eq', 'fx_gcd_norm_eq'), ('fx_ditheredbw', 'fx_ditheredbw', 'fx_ditheredbw'), ('fx_engrave', 'fx_engrave', 'fx_engrave'), ('Engrave_colore', 'Engrave_colore', 'Engrave_colore'), ('engrave_modifie', 'engrave_modifie', 'engrave_modifie'), ('fx_freaky_bw', 'fx_freaky_bw', 'fx_freaky_bw'), ('XY_hardsketchbw_samj_en', 'XY_hardsketchbw_samj_en', 'XY_hardsketchbw_samj_en'), ('XY_hardsketchbw_samj', 'XY_hardsketchbw_samj', 'XY_hardsketchbw_samj'), ('fx_ink_wash', 'fx_ink_wash', 'fx_ink_wash'), ('fx_gcd_layeretch', 'fx_gcd_layeretch', 'fx_gcd_layeretch'), ('fx_pencilbw', 'fx_pencilbw', 'fx_pencilbw'), ('fx_pencil_portraitbw', 'fx_pencil_portraitbw', 'fx_pencil_portraitbw'), ('samj_NB_EdgesO_Engrave', 'samj_NB_EdgesO_Engrave', 'samj_NB_EdgesO_Engrave'), ('samj_scintillements', 'samj_scintillements', 'samj_scintillements'), ('fx_stamp', 'fx_stamp', 'fx_stamp'), ('fx_gcd_etch', 'fx_gcd_etch', 'fx_gcd_etch')) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb19.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator19(bpy.types.Operator):
    bl_idname = "object.gmic_operator19"
    bl_label = "Black & White"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb19)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb19.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb20(self, context):
    l = (('fx_remove_scratches', 'fx_remove_scratches', 'fx_remove_scratches'),) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb20.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator20(bpy.types.Operator):
    bl_idname = "object.gmic_operator20"
    bl_label = "Chris From Pixls"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb20)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb20.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb21(self, context):
    l = (('fx_color_abstraction', 'fx_color_abstraction', 'fx_color_abstraction'), ('fx_apply_haldclut', 'fx_apply_haldclut', 'fx_apply_haldclut'), ('fx_adjust_colors', 'fx_adjust_colors', 'fx_adjust_colors'), ('fx_boost_chroma', 'fx_boost_chroma', 'fx_boost_chroma'), ('fx_boost_fade', 'fx_boost_fade', 'fx_boost_fade'), ('fx_channel_processing', 'fx_channel_processing', 'fx_channel_processing'), ('fx_channels2layers', 'fx_channels2layers', 'fx_channels2layers'), ('fx_clut_from_ab', 'fx_clut_from_ab', 'fx_clut_from_ab'), ('iain_cmyk_tone_p', 'iain_cmyk_tone_p', 'iain_cmyk_tone_p'), ('fx_balance_gamma', 'fx_balance_gamma', 'fx_balance_gamma'), ('colorblind', 'colorblind', 'colorblind'), ('jl_colorgrading', 'jl_colorgrading', 'jl_colorgrading'), ('samj_Color_Palettes', 'samj_Color_Palettes', 'samj_Color_Palettes'), ('fx_mask_color', 'fx_mask_color', 'fx_mask_color'), ('fx_color_presets', 'fx_color_presets', 'fx_color_presets'), ('fx_tk_colortemp', 'fx_tk_colortemp', 'fx_tk_colortemp'), ('fx_colorful_blobs', 'fx_colorful_blobs', 'fx_colorful_blobs'), ('fx_colormap', 'fx_colormap', 'fx_colormap'), ('csswap', 'csswap', 'csswap'), ('Couleurs_Metalliques_samj_en', 'Couleurs_Metalliques_samj_en', 'Couleurs_Metalliques_samj_en'), ('Couleurs_Metalliques', 'Couleurs_Metalliques', 'Couleurs_Metalliques'), ('fx_cubehelix', 'fx_cubehelix', 'fx_cubehelix'), ('fx_curves_interactive', 'fx_curves_interactive', 'fx_curves_interactive'), ('fx_customize_clut', 'fx_customize_clut', 'fx_customize_clut'), ('fx_darken_sky', 'fx_darken_sky', 'fx_darken_sky'), ('fx_decompose_channels', 'fx_decompose_channels', 'fx_decompose_channels'), ('fx_detect_skin', 'fx_detect_skin', 'fx_detect_skin'), ('fx_equalize_hsv', 'fx_equalize_hsv', 'fx_equalize_hsv'), ('fx_hsv_equalizer', 'fx_hsv_equalizer', 'fx_hsv_equalizer'), ('fx_frequency_representation', 'fx_frequency_representation', 'fx_frequency_representation'), ('gcd_hsl', 'gcd_hsl', 'gcd_hsl'), ('gcd_hsv_select', 'gcd_hsv_select', 'gcd_hsv_select'), ('iain_hue_light_dark_p', 'iain_hue_light_dark_p', 'iain_hue_light_dark_p'), ('fx_tk_metallic', 'fx_tk_metallic', 'fx_tk_metallic'), ('fx_mix_cmyk', 'fx_mix_cmyk', 'fx_mix_cmyk'), ('fx_mix_hsv', 'fx_mix_hsv', 'fx_mix_hsv'), ('fx_mix_lab', 'fx_mix_lab', 'fx_mix_lab'), ('fx_mix_pca', 'fx_mix_pca', 'fx_mix_pca'), ('fx_mix_rgb', 'fx_mix_rgb', 'fx_mix_rgb'), ('fx_mix_ycbcr', 'fx_mix_ycbcr', 'fx_mix_ycbcr'), ('jr_desaturate', 'jr_desaturate', 'jr_desaturate'), ('fx_retinex', 'fx_retinex', 'fx_retinex'), ('fx_retrofade', 'fx_retrofade', 'fx_retrofade'), ('iain_rgb_tone', 'iain_rgb_tone', 'iain_rgb_tone'), ('samj_At06A_2017_VarCouleurs', 'samj_At06A_2017_VarCouleurs', 'samj_At06A_2017_VarCouleurs'), ('samj_Valeur_Moyenne_LCH', 'samj_Valeur_Moyenne_LCH', 'samj_Valeur_Moyenne_LCH'), ('samj_Variations_RVB', 'samj_Variations_RVB', 'samj_Variations_RVB'), ('fx_satellite', 'fx_satellite', 'fx_satellite'), ('Saturation_EQ_p', 'Saturation_EQ_p', 'Saturation_EQ_p'), ('fx_select_color', 'fx_select_color', 'fx_select_color'), ('fx_selective_desaturation', 'fx_selective_desaturation', 'fx_selective_desaturation'), ('fx_sepia', 'fx_sepia', 'fx_sepia'), ('fx_simulate_film', 'fx_simulate_film', 'fx_simulate_film'), ('gcd_hio_levels', 'gcd_hio_levels', 'gcd_hio_levels'), ('iain_tone_presets_p', 'iain_tone_presets_p', 'iain_tone_presets_p'), ('fx_transfer_histogram', 'fx_transfer_histogram', 'fx_transfer_histogram'), ('fx_gcd_transfer_colors_patch', 'fx_gcd_transfer_colors_patch', 'fx_gcd_transfer_colors_patch'), ('fx_transfer_pca', 'fx_transfer_pca', 'fx_transfer_pca'), ('fx_transfer_rgb', 'fx_transfer_rgb', 'fx_transfer_rgb'), ('fx_custom_transform', 'fx_custom_transform', 'fx_custom_transform'), ('fx_tk_vintage', 'fx_tk_vintage', 'fx_tk_vintage'), ('fx_zonesystem', 'fx_zonesystem', 'fx_zonesystem')) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb21.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator21(bpy.types.Operator):
    bl_idname = "object.gmic_operator21"
    bl_label = "Colors"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb21)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb21.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb22(self, context):
    l = (('fx_convolve', 'fx_convolve', 'fx_convolve'), ('fx_curvature', 'fx_curvature', 'fx_curvature'), ('fx_dog', 'fx_dog', 'fx_dog'), ('fx_distance', 'fx_distance', 'fx_distance'), ('fx_edges', 'fx_edges', 'fx_edges'), ('fx_edge_offsets', 'fx_edge_offsets', 'fx_edge_offsets'), ('fx_extract_foreground', 'fx_extract_foreground', 'fx_extract_foreground'), ('fx_gradient_norm', 'fx_gradient_norm', 'fx_gradient_norm'), ('fx_jr_gradient_norm', 'fx_jr_gradient_norm', 'fx_jr_gradient_norm'), ('fx_gradient2rgb', 'fx_gradient2rgb', 'fx_gradient2rgb'), ('fx_isophotes', 'fx_isophotes', 'fx_isophotes'), ('fx_laplacian', 'fx_laplacian', 'fx_laplacian'), ('fx_local_orientation', 'fx_local_orientation', 'fx_local_orientation'), ('fx_morphological', 'fx_morphological', 'fx_morphological'), ('samj_Carte_De_Repoussage', 'samj_Carte_De_Repoussage', 'samj_Carte_De_Repoussage'), ('samj_Colored_Outlines', 'samj_Colored_Outlines', 'samj_Colored_Outlines'), ('samj_Coloriage', 'samj_Coloriage', 'samj_Coloriage'), ('samj_Contours_Arrondis', 'samj_Contours_Arrondis', 'samj_Contours_Arrondis'), ('samj_Contours_Blancs', 'samj_Contours_Blancs', 'samj_Contours_Blancs'), ('samj_Contours_Colores', 'samj_Contours_Colores', 'samj_Contours_Colores'), ('samj_Quelques_Isophotes', 'samj_Quelques_Isophotes', 'samj_Quelques_Isophotes'), ('samj_Quelques_Isophotes_B', 'samj_Quelques_Isophotes_B', 'samj_Quelques_Isophotes_B'), ('samj_Scintillements_Colores_Contours', 'samj_Scintillements_Colores_Contours', 'samj_Scintillements_Colores_Contours'), ('samj_Skeletation', 'samj_Skeletation', 'samj_Skeletation'), ('samj_Test_Mauvais_Contours', 'samj_Test_Mauvais_Contours', 'samj_Test_Mauvais_Contours'), ('fx_segment_watershed', 'fx_segment_watershed', 'fx_segment_watershed'), ('fx_skeleton', 'fx_skeleton', 'fx_skeleton'), ('fx_superpixels', 'fx_superpixels', 'fx_superpixels'), ('fx_thin_edges', 'fx_thin_edges', 'fx_thin_edges')) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb22.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator22(bpy.types.Operator):
    bl_idname = "object.gmic_operator22"
    bl_label = "Contours"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb22)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb22.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb23(self, context):
    l = (('fx_corvo_painting_5', 'fx_corvo_painting_5', 'fx_corvo_painting_5'),) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb23.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator23(bpy.types.Operator):
    bl_idname = "object.gmic_operator23"
    bl_label = "Corvo"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb23)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb23.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb24(self, context):
    l = (('fx_apply_Labcurve', 'fx_apply_Labcurve', 'fx_apply_Labcurve'), ('fx_apply_Labcurve', 'fx_apply_Labcurve', 'fx_apply_Labcurve'), ('fx_apply_Labcurve', 'fx_apply_Labcurve', 'fx_apply_Labcurve')) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb24.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator24(bpy.types.Operator):
    bl_idname = "object.gmic_operator24"
    bl_label = "Curves [Lab]"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb24)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb24.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb25(self, context):
    l = (('fx_apply_RGBcurve', 'fx_apply_RGBcurve', 'fx_apply_RGBcurve'), ('fx_apply_RGBcurve', 'fx_apply_RGBcurve', 'fx_apply_RGBcurve'), ('fx_apply_RGBcurve', 'fx_apply_RGBcurve', 'fx_apply_RGBcurve')) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb25.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator25(bpy.types.Operator):
    bl_idname = "object.gmic_operator25"
    bl_label = "Curves [RGB]"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb25)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb25.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb26(self, context):
    l = (('fx_apply_YCbCrcurve', 'fx_apply_YCbCrcurve', 'fx_apply_YCbCrcurve'), ('fx_apply_YCbCrcurve', 'fx_apply_YCbCrcurve', 'fx_apply_YCbCrcurve'), ('fx_apply_YCbCrcurve', 'fx_apply_YCbCrcurve', 'fx_apply_YCbCrcurve')) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb26.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator26(bpy.types.Operator):
    bl_idname = "object.gmic_operator26"
    bl_label = "Curves [YCbCr]"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb26)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb26.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb27(self, context):
    l = (('fx_auto_gnarl', 'fx_auto_gnarl', 'fx_auto_gnarl'), ('fx_buffer_destroyer', 'fx_buffer_destroyer', 'fx_buffer_destroyer'), ('fx_buffer_error', 'fx_buffer_error', 'fx_buffer_error'), ('fx_custom_deformation', 'fx_custom_deformation', 'fx_custom_deformation'), ('fx_circle_transform', 'fx_circle_transform', 'fx_circle_transform'), ('fx_conformal_maps', 'fx_conformal_maps', 'fx_conformal_maps'), ('souphead_droste10', 'souphead_droste10', 'souphead_droste10'), ('fx_crease', 'fx_crease', 'fx_crease'), ('fx_distort_lens', 'fx_distort_lens', 'fx_distort_lens'), ('fx_drop_water', 'fx_drop_water', 'fx_drop_water'), ('fx_equirectangular2nadirzenith', 'fx_equirectangular2nadirzenith', 'fx_equirectangular2nadirzenith'), ('fx_euclidean2polar', 'fx_euclidean2polar', 'fx_euclidean2polar'), ('fisheye', 'fisheye', 'fisheye'), ('fx_flower', 'fx_flower', 'fx_flower'), ('fx_rotoidoscope', 'fx_rotoidoscope', 'fx_rotoidoscope'), ('fx_kaleidoscope', 'fx_kaleidoscope', 'fx_kaleidoscope'), ('fx_symmetrizoscope', 'fx_symmetrizoscope', 'fx_symmetrizoscope'), ('fx_jr_klc', 'fx_jr_klc', 'fx_jr_klc'), ('fx_layer_cake', 'fx_layer_cake', 'fx_layer_cake'), ('fx_layer_cake_2', 'fx_layer_cake_2', 'fx_layer_cake_2'), ('fx_morph_interactive', 'fx_morph_interactive', 'fx_morph_interactive'), ('fx_warp_perspective', 'fx_warp_perspective', 'fx_warp_perspective'), ('fx_transform_polar', 'fx_transform_polar', 'fx_transform_polar'), ('fx_powertwirl', 'fx_powertwirl', 'fx_powertwirl'), ('fx_quadrangle', 'fx_quadrangle', 'fx_quadrangle'), ('raindrops', 'raindrops', 'raindrops'), ('deform', 'deform', 'deform'), ('fx_jr_deform', 'fx_jr_deform', 'fx_jr_deform'), ('samj_Random_Small_Deformations', 'samj_Random_Small_Deformations', 'samj_Random_Small_Deformations'), ('fx_rays_from_image', 'fx_rays_from_image', 'fx_rays_from_image'), ('fx_reflect', 'fx_reflect', 'fx_reflect'), ('ripple', 'ripple', 'ripple'), ('samj_Cercle_Polaire', 'samj_Cercle_Polaire', 'samj_Cercle_Polaire'), ('samj_Ecraser_Etirer', 'samj_Ecraser_Etirer', 'samj_Ecraser_Etirer'), ('samj_Ecraser_Etirer_V2', 'samj_Ecraser_Etirer_V2', 'samj_Ecraser_Etirer_V2'), ('fx_seamcarve', 'fx_seamcarve', 'fx_seamcarve'), ('fx_shifter', 'fx_shifter', 'fx_shifter'), ('fx_map_sphere', 'fx_map_sphere', 'fx_map_sphere'), ('fx_spherize', 'fx_spherize', 'fx_spherize'), ('fx_jr_spiral_transform', 'fx_jr_spiral_transform', 'fx_jr_spiral_transform'), ('fx_square_circle', 'fx_square_circle', 'fx_square_circle'), ('fx_project_stereographic', 'fx_project_stereographic', 'fx_project_stereographic'), ('fx_symmetrize', 'fx_symmetrize', 'fx_symmetrize'), ('fx_textured_glass', 'fx_textured_glass', 'fx_textured_glass'), ('fx_twirl', 'fx_twirl', 'fx_twirl'), ('fx_ultrawarptwo', 'fx_ultrawarptwo', 'fx_ultrawarptwo'), ('fx_ultrawarp4plus', 'fx_ultrawarp4plus', 'fx_ultrawarp4plus'), ('fx_warp_interactive', 'fx_warp_interactive', 'fx_warp_interactive'), ('water', 'water', 'water'), ('wave', 'wave', 'wave'), ('fx_wind', 'fx_wind', 'fx_wind'), ('fx_zoom', 'fx_zoom', 'fx_zoom')) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb27.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator27(bpy.types.Operator):
    bl_idname = "object.gmic_operator27"
    bl_label = "Deformations"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb27)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb27.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb28(self, context):
    l = (('fx_simulate_grain', 'fx_simulate_grain', 'fx_simulate_grain'), ('fx_blur_angular', 'fx_blur_angular', 'fx_blur_angular'), ('fx_blur_bloom_glare', 'fx_blur_bloom_glare', 'fx_blur_bloom_glare'), ('fx_blur_bloom', 'fx_blur_bloom', 'fx_blur_bloom'), ('fx_blur_dof', 'fx_blur_dof', 'fx_blur_dof'), ('fx_gaussian_blur', 'fx_gaussian_blur', 'fx_gaussian_blur'), ('fx_glow', 'fx_glow', 'fx_glow'), ('fx_blur_linear', 'fx_blur_linear', 'fx_blur_linear'), ('fx_blur_radial', 'fx_blur_radial', 'fx_blur_radial'), ('fx_blend_bomb', 'fx_blend_bomb', 'fx_blend_bomb'), ('fx_texture_afre_broken', 'fx_texture_afre_broken', 'fx_texture_afre_broken'), ('fx_butterworth_bp', 'fx_butterworth_bp', 'fx_butterworth_bp'), ('fx_self_glitching_cascade', 'fx_self_glitching_cascade', 'fx_self_glitching_cascade'), ('fx_chromatic_aberrations', 'fx_chromatic_aberrations', 'fx_chromatic_aberrations'), ('fx_gcd_crt', 'fx_gcd_crt', 'fx_gcd_crt'), ('fx_dct_fsu', 'fx_dct_fsu', 'fx_dct_fsu'), ('samj_Zones_Grises_en', 'samj_Zones_Grises_en', 'samj_Zones_Grises_en'), ('fx_dirty', 'fx_dirty', 'fx_dirty'), ('fx_jfif_fake', 'fx_jfif_fake', 'fx_jfif_fake'), ('fx_qam_glitch', 'fx_qam_glitch', 'fx_qam_glitch'), ('fx_flip_blocs', 'fx_flip_blocs', 'fx_flip_blocs'), ('fx_jfif_bomb', 'fx_jfif_bomb', 'fx_jfif_bomb'), ('fx_jfif', 'fx_jfif', 'fx_jfif'), ('fx_jfif_xt', 'fx_jfif_xt', 'fx_jfif_xt'), ('fx_jpeg_artefacts', 'fx_jpeg_artefacts', 'fx_jpeg_artefacts'), ('fx_lomo', 'fx_lomo', 'fx_lomo'), ('fx_mess_with_bits', 'fx_mess_with_bits', 'fx_mess_with_bits'), ('fx_noise', 'fx_noise', 'fx_noise'), ('fx_noise', 'fx_noise', 'fx_noise'), ('fx_noise_perlin', 'fx_noise_perlin', 'fx_noise_perlin'), ('fx_spread', 'fx_spread', 'fx_spread'), ('fx_stripes_y', 'fx_stripes_y', 'fx_stripes_y'), ('fx_8bits', 'fx_8bits', 'fx_8bits'), ('samj_Degradations_Path_Solidify', 'samj_Degradations_Path_Solidify', 'samj_Degradations_Path_Solidify'), ('fx_pixelsort', 'fx_pixelsort', 'fx_pixelsort'), ('pseudo_ecb', 'pseudo_ecb', 'pseudo_ecb'), ('fx_rain', 'fx_rain', 'fx_rain'), ('samj_Random_Plasma', 'samj_Random_Plasma', 'samj_Random_Plasma'), ('fx_shade_stripes', 'fx_shade_stripes', 'fx_shade_stripes'), ('fx_row_shift', 'fx_row_shift', 'fx_row_shift'), ('samj_Ellipses_Inpaint', 'samj_Ellipses_Inpaint', 'samj_Ellipses_Inpaint'), ('samj_Zones_Grises', 'samj_Zones_Grises', 'samj_Zones_Grises'), ('sawtoother_cmy_k', 'sawtoother_cmy_k', 'sawtoother_cmy_k'), ('sawtoother_hsx', 'sawtoother_hsx', 'sawtoother_hsx'), ('sawtoother_lab8', 'sawtoother_lab8', 'sawtoother_lab8'), ('sawtoother_lch8', 'sawtoother_lch8', 'sawtoother_lch8'), ('sawtoother_rgb', 'sawtoother_rgb', 'sawtoother_rgb'), ('sawtoother_srgb', 'sawtoother_srgb', 'sawtoother_srgb'), ('sawtoother_xyz8', 'sawtoother_xyz8', 'sawtoother_xyz8'), ('sawtoother_ycbcr', 'sawtoother_ycbcr', 'sawtoother_ycbcr'), ('sawtoother_yiq8', 'sawtoother_yiq8', 'sawtoother_yiq8'), ('sawtoother_yuv8', 'sawtoother_yuv8', 'sawtoother_yuv8'), ('fx_scanlines', 'fx_scanlines', 'fx_scanlines'), ('fx_self_glitching', 'fx_self_glitching', 'fx_self_glitching'), ('fx_shredder', 'fx_shredder', 'fx_shredder'), ('fx_jr_smooth_eq', 'fx_jr_smooth_eq', 'fx_jr_smooth_eq'), ('fx_streak', 'fx_streak', 'fx_streak'), ('fx_superstreak', 'fx_superstreak', 'fx_superstreak'), ('fx_watermark_visible', 'fx_watermark_visible', 'fx_watermark_visible'), ('fx_warp_by_intensity', 'fx_warp_by_intensity', 'fx_warp_by_intensity')) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb28.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator28(bpy.types.Operator):
    bl_idname = "object.gmic_operator28"
    bl_label = "Degradations"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb28)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb28.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb29(self, context):
    l = (('fx_morpho', 'fx_morpho', 'fx_morpho'),) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb29.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator29(bpy.types.Operator):
    bl_idname = "object.gmic_operator29"
    bl_label = "Deprecated"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb29)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb29.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb30(self, context):
    l = (('fx_bitplane8', 'fx_bitplane8', 'fx_bitplane8'), ('fx_jr_bilinear', 'fx_jr_bilinear', 'fx_jr_bilinear'), ('iain_constrained_sharpen', 'iain_constrained_sharpen', 'iain_constrained_sharpen'), ('jeje_dehaze', 'jeje_dehaze', 'jeje_dehaze'), ('fx_equalize_details', 'fx_equalize_details', 'fx_equalize_details'), ('fx_tk_dri', 'fx_tk_dri', 'fx_tk_dri'), ('fx_equalize_local_histograms', 'fx_equalize_local_histograms', 'fx_equalize_local_histograms'), ('fx_freaky_details', 'fx_freaky_details', 'fx_freaky_details'), ('fx_highpass', 'fx_highpass', 'fx_highpass'), ('fx_LCE', 'fx_LCE', 'fx_LCE'), ('fx_normalize_local', 'fx_normalize_local', 'fx_normalize_local'), ('fx_local_processing', 'fx_local_processing', 'fx_local_processing'), ('jeje_normalize_local_variance', 'jeje_normalize_local_variance', 'jeje_normalize_local_variance'), ('fx_magic_details', 'fx_magic_details', 'fx_magic_details'), ('make_up', 'make_up', 'make_up'), ('fx_tk_mask', 'fx_tk_mask', 'fx_tk_mask'), ('fx_mighty_details', 'fx_mighty_details', 'fx_mighty_details'), ('fx_tk_portrait', 'fx_tk_portrait', 'fx_tk_portrait'), ('iain_pyramid_processing', 'iain_pyramid_processing', 'iain_pyramid_processing'), ('samj_Antialias_Wavelet', 'samj_Antialias_Wavelet', 'samj_Antialias_Wavelet'), ('fx_deblur', 'fx_deblur', 'fx_deblur'), ('fx_unsharp_goldmeinel', 'fx_unsharp_goldmeinel', 'fx_unsharp_goldmeinel'), ('jeje_hessian_sharpen', 'jeje_hessian_sharpen', 'jeje_hessian_sharpen'), ('fx_sharpen_inversediff', 'fx_sharpen_inversediff', 'fx_sharpen_inversediff'), ('fx_sharpen_multiscale', 'fx_sharpen_multiscale', 'fx_sharpen_multiscale'), ('fx_unsharp_octave', 'fx_unsharp_octave', 'fx_unsharp_octave'), ('fx_unsharp_richardsonlucy', 'fx_unsharp_richardsonlucy', 'fx_unsharp_richardsonlucy'), ('fx_sharpen_shock', 'fx_sharpen_shock', 'fx_sharpen_shock'), ('fx_sharpen_texture', 'fx_sharpen_texture', 'fx_sharpen_texture'), ('fx_unsharp', 'fx_unsharp', 'fx_unsharp'), ('samj_Wavelet_Sharpen_Test_en', 'samj_Wavelet_Sharpen_Test_en', 'samj_Wavelet_Sharpen_Test_en'), ('jeje_whiten_frequency', 'jeje_whiten_frequency', 'jeje_whiten_frequency'), ('fx_split_details_alpha', 'fx_split_details_alpha', 'fx_split_details_alpha'), ('fx_split_details_gaussian', 'fx_split_details_gaussian', 'fx_split_details_gaussian'), ('fx_split_details_wavelets', 'fx_split_details_wavelets', 'fx_split_details_wavelets'), ('jeje_spotify', 'jeje_spotify', 'jeje_spotify'), ('iain_texture_enhance_p', 'iain_texture_enhance_p', 'iain_texture_enhance_p'), ('gcd_tone_enhance', 'gcd_tone_enhance', 'gcd_tone_enhance'), ('fx_map_tones', 'fx_map_tones', 'fx_map_tones'), ('fx_map_tones_fast', 'fx_map_tones_fast', 'fx_map_tones_fast'), ('samj_Wavelet_Sharpen_Test', 'samj_Wavelet_Sharpen_Test', 'samj_Wavelet_Sharpen_Test'), ('fx_yag_soften', 'fx_yag_soften', 'fx_yag_soften')) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb30.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator30(bpy.types.Operator):
    bl_idname = "object.gmic_operator30"
    bl_label = "Details"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb30)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb30.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb31(self, context):
    l = (('fx_droste', 'fx_droste', 'fx_droste'), ('fx_frame_blur', 'fx_frame_blur', 'fx_frame_blur'), ('frame_cube', 'frame_cube', 'frame_cube'), ('fx_frame_fuzzy', 'fx_frame_fuzzy', 'fx_frame_fuzzy'), ('fx_frame_mirror', 'fx_frame_mirror', 'fx_frame_mirror'), ('fx_frame_painting', 'fx_frame_painting', 'fx_frame_painting'), ('fx_frame_pattern', 'fx_frame_pattern', 'fx_frame_pattern'), ('fx_frame', 'fx_frame', 'fx_frame'), ('fx_frame_round', 'fx_frame_round', 'fx_frame_round'), ('fx_frame_smooth', 'fx_frame_smooth', 'fx_frame_smooth'), ('fx_old_photo', 'fx_old_photo', 'fx_old_photo'), ('fx_polaroid', 'fx_polaroid', 'fx_polaroid'), ('samj_At06A_2017_frame_painting', 'samj_At06A_2017_frame_painting', 'samj_At06A_2017_frame_painting'), ('fx_tunnel', 'fx_tunnel', 'fx_tunnel'), ('fx_vignette', 'fx_vignette', 'fx_vignette')) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb31.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator31(bpy.types.Operator):
    bl_idname = "object.gmic_operator31"
    bl_label = "Frames"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb31)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb31.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb32(self, context):
    l = (('fx_bandpass', 'fx_bandpass', 'fx_bandpass'), ('fx_display_fft', 'fx_display_fft', 'fx_display_fft'), ('fx_fourier', 'fx_fourier', 'fx_fourier'), ('fx_watermark_fourier', 'fx_watermark_fourier', 'fx_watermark_fourier')) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb32.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator32(bpy.types.Operator):
    bl_idname = "object.gmic_operator32"
    bl_label = "Frequencies"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb32)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb32.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb33(self, context):
    l = (('gcd_anti_alias', 'gcd_anti_alias', 'gcd_anti_alias'), ('gcd_auto_balance', 'gcd_auto_balance', 'gcd_auto_balance'), ('gcd_blend_feather', 'gcd_blend_feather', 'gcd_blend_feather'), ('gcd_comp_blur', 'gcd_comp_blur', 'gcd_comp_blur'), ('fx_gcd_crmt_tile', 'fx_gcd_crmt_tile', 'fx_gcd_crmt_tile'), ('fx_gcd_cumul_math', 'fx_gcd_cumul_math', 'fx_gcd_cumul_math'), ('fx_gcd_blur_deblur_texture', 'fx_gcd_blur_deblur_texture', 'fx_gcd_blur_deblur_texture'), ('gcd_depth_blur', 'gcd_depth_blur', 'gcd_depth_blur'), ('gcd_emboss', 'gcd_emboss', 'gcd_emboss'), ('gcd_geometric_balance', 'gcd_geometric_balance', 'gcd_geometric_balance'), ('gcd_infomap', 'gcd_infomap', 'gcd_infomap'), ('gcd_ebwarp', 'gcd_ebwarp', 'gcd_ebwarp'), ('gcd_jpeg_smooth', 'gcd_jpeg_smooth', 'gcd_jpeg_smooth'), ('gcd_layers', 'gcd_layers', 'gcd_layers'), ('gcd_balance_lms', 'gcd_balance_lms', 'gcd_balance_lms'), ('gcd_fx_local_fmean', 'gcd_fx_local_fmean', 'gcd_fx_local_fmean'), ('tran_multi_threshold', 'tran_multi_threshold', 'tran_multi_threshold'), ('gcd_normalize_brightness', 'gcd_normalize_brightness', 'gcd_normalize_brightness'), ('gcd_pqct', 'gcd_pqct', 'gcd_pqct'), ('fx_gcd_quicktone', 'fx_gcd_quicktone', 'fx_gcd_quicktone'), ('gcd_recol', 'gcd_recol', 'gcd_recol'), ('gcd_sharpen_gradient', 'gcd_sharpen_gradient', 'gcd_sharpen_gradient'), ('gcd_sharpen_tones', 'gcd_sharpen_tones', 'gcd_sharpen_tones'), ('gcd_srotate', 'gcd_srotate', 'gcd_srotate'), ('fx_gcd_geometric_median', 'fx_gcd_geometric_median', 'fx_gcd_geometric_median'), ('gcd_splitobj', 'gcd_splitobj', 'gcd_splitobj'), ('gcd_stereo_vid', 'gcd_stereo_vid', 'gcd_stereo_vid'), ('gcd_temp_balance', 'gcd_temp_balance', 'gcd_temp_balance'), ('gcd_unquantize', 'gcd_unquantize', 'gcd_unquantize'), ('gcd_upscale_box', 'gcd_upscale_box', 'gcd_upscale_box'), ('gcd_upscale_noise', 'gcd_upscale_noise', 'gcd_upscale_noise'), ('gcd_warpmap', 'gcd_warpmap', 'gcd_warpmap'), ('gcd_wiremap', 'gcd_wiremap', 'gcd_wiremap'), ('gcd_xbr2x', 'gcd_xbr2x', 'gcd_xbr2x')) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb33.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator33(bpy.types.Operator):
    bl_idname = "object.gmic_operator33"
    bl_label = "Garagecoder"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb33)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb33.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb34(self, context):
    l = (('fx_gb_cfx', 'fx_gb_cfx', 'fx_gb_cfx'), ('_none_', '_none_', '_none_'), ('fx_gb_lb', 'fx_gb_lb', 'fx_gb_lb'), ('fx_gb_mp', 'fx_gb_mp', 'fx_gb_mp'), ('fx_gb_mcfx', 'fx_gb_mcfx', 'fx_gb_mcfx'), ('fx_gb_pp', 'fx_gb_pp', 'fx_gb_pp'), ('fx_gb_ub', 'fx_gb_ub', 'fx_gb_ub')) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb34.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator34(bpy.types.Operator):
    bl_idname = "object.gmic_operator34"
    bl_label = "Gentlemanbeggar"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb34)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb34.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb35(self, context):
    l = (('gtutor_blur_img', 'gtutor_blur_img', 'gtutor_blur_img'), ('hedcut', 'hedcut', 'hedcut')) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb35.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator35(bpy.types.Operator):
    bl_idname = "object.gmic_operator35"
    bl_label = "Gmic Tutorials"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb35)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb35.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb36(self, context):
    l = (('iain_2d_scopes', 'iain_2d_scopes', 'iain_2d_scopes'), ('iain_smooth_tutorial', 'iain_smooth_tutorial', 'iain_smooth_tutorial'), ('iain_auto_wb', 'iain_auto_wb', 'iain_auto_wb'), ('automixer', 'automixer', 'automixer'), ('iain_brown_spot_clean', 'iain_brown_spot_clean', 'iain_brown_spot_clean'), ('iain_CA_correction', 'iain_CA_correction', 'iain_CA_correction'), ('iain_detect_moire', 'iain_detect_moire', 'iain_detect_moire'), ('iain_easy_skin_retouch', 'iain_easy_skin_retouch', 'iain_easy_skin_retouch'), ('exfuse', 'exfuse', 'exfuse'), ('exfusion', 'exfusion', 'exfusion'), ('exfusion3', 'exfusion3', 'exfusion3'), ('exfusion5', 'exfusion5', 'exfusion5'), ('iain_fast_formula', 'iain_fast_formula', 'iain_fast_formula'), ('iain_fast_median_stack', 'iain_fast_median_stack', 'iain_fast_median_stack'), ('fft_tile', 'fft_tile', 'fft_tile'), ('fill_holes', 'fill_holes', 'fill_holes'), ('iain_descreen2', 'iain_descreen2', 'iain_descreen2'), ('iain_halftone_shapes', 'iain_halftone_shapes', 'iain_halftone_shapes'), ('iain_hearttone', 'iain_hearttone', 'iain_hearttone'), ('iain_2x', 'iain_2x', 'iain_2x'), ('iain_demosiac', 'iain_demosiac', 'iain_demosiac'), ('iain_denoise_2019_beta3', 'iain_denoise_2019_beta3', 'iain_denoise_2019_beta3'), ('iain_remove_pattern', 'iain_remove_pattern', 'iain_remove_pattern'), ('iain_star_burst', 'iain_star_burst', 'iain_star_burst'), ('iain_unindex', 'iain_unindex', 'iain_unindex'), ('iain_weightmap', 'iain_weightmap', 'iain_weightmap'), ('iain_iains_nr', 'iain_iains_nr', 'iain_iains_nr'), ('iain_iid_demosaic', 'iain_iid_demosaic', 'iain_iid_demosaic'), ('luminance_nr', 'luminance_nr', 'luminance_nr'), ('luminance_nr_two', 'luminance_nr_two', 'luminance_nr_two'), ('iain_minimum_chroma_demosaic', 'iain_minimum_chroma_demosaic', 'iain_minimum_chroma_demosaic'), ('iain_moire_removal', 'iain_moire_removal', 'iain_moire_removal'), ('iain_moire_removal_NP', 'iain_moire_removal_NP', 'iain_moire_removal_NP'), ('ms_nlmeans_c_noise2_p', 'ms_nlmeans_c_noise2_p', 'ms_nlmeans_c_noise2_p'), ('ms_patch_c', 'ms_patch_c', 'ms_patch_c'), ('MS_Patch_NR', 'MS_Patch_NR', 'MS_Patch_NR'), ('MS_Patch_NR3', 'MS_Patch_NR3', 'MS_Patch_NR3'), ('ms_patch_smooth', 'ms_patch_smooth', 'ms_patch_smooth'), ('ms_smooth', 'ms_smooth', 'ms_smooth'), ('nr3', 'nr3', 'nr3'), ('nr5', 'nr5', 'nr5'), ('iain_png_processing', 'iain_png_processing', 'iain_png_processing'), ('iain_savenoiseprint', 'iain_savenoiseprint', 'iain_savenoiseprint'), ('simplelocalcontrast_p', 'simplelocalcontrast_p', 'simplelocalcontrast_p'), ('iain_fx_skin_mask', 'iain_fx_skin_mask', 'iain_fx_skin_mask'), ('iain_smartdemos', 'iain_smartdemos', 'iain_smartdemos'), ('iain_split_orientation', 'iain_split_orientation', 'iain_split_orientation'), ('spot_mask', 'spot_mask', 'spot_mask'), ('star_tone', 'star_tone', 'star_tone'), ('iain_sub_cast', 'iain_sub_cast', 'iain_sub_cast'), ('iain_turbulent_halftone', 'iain_turbulent_halftone', 'iain_turbulent_halftone')) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb36.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator36(bpy.types.Operator):
    bl_idname = "object.gmic_operator36"
    bl_label = "Iain Fergusson"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb36)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb36.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb37(self, context):
    l = (('mc_flip', 'mc_flip', 'mc_flip'), ('mc_information', 'mc_information', 'mc_information'), ('mc_mail', 'mc_mail', 'mc_mail'), ('mc_phone', 'mc_phone', 'mc_phone'), ('mc_shopping_cart', 'mc_shopping_cart', 'mc_shopping_cart')) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb37.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator37(bpy.types.Operator):
    bl_idname = "object.gmic_operator37"
    bl_label = "Icons"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb37)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb37.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb38(self, context):
    l = (('jeje_render3d', 'jeje_render3d', 'jeje_render3d'), ('jeje_deconvolve', 'jeje_deconvolve', 'jeje_deconvolve'), ('jeje_zernike_preview', 'jeje_zernike_preview', 'jeje_zernike_preview')) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb38.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator38(bpy.types.Operator):
    bl_idname = "object.gmic_operator38"
    bl_label = "JéJé"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb38)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb38.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb39(self, context):
    l = (('_none_', '_none_', '_none_'), ('jpr_colourillusion', 'jpr_colourillusion', 'jpr_colourillusion'), ('jpr_coltexindex', 'jpr_coltexindex', 'jpr_coltexindex'), ('jpr_decimate', 'jpr_decimate', 'jpr_decimate'), ('jpr_gradient_smooth', 'jpr_gradient_smooth', 'jpr_gradient_smooth'), ('jpr_line_edges', 'jpr_line_edges', 'jpr_line_edges'), ('jpr_orientedthinning', 'jpr_orientedthinning', 'jpr_orientedthinning'), ('jpr_phasecongruence', 'jpr_phasecongruence', 'jpr_phasecongruence'), ('jpr_remove_blocks1', 'jpr_remove_blocks1', 'jpr_remove_blocks1'), ('jpr_shapes_gradient', 'jpr_shapes_gradient', 'jpr_shapes_gradient'), ('jpr_specularbumps', 'jpr_specularbumps', 'jpr_specularbumps'), ('jpr_warpfromthreshold', 'jpr_warpfromthreshold', 'jpr_warpfromthreshold')) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb39.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator39(bpy.types.Operator):
    bl_idname = "object.gmic_operator39"
    bl_label = "Jayprich"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb39)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb39.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb40(self, context):
    l = (('fx_mesh_blend', 'fx_mesh_blend', 'fx_mesh_blend'),) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb40.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator40(bpy.types.Operator):
    bl_idname = "object.gmic_operator40"
    bl_label = "Joan Rake"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb40)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb40.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb41(self, context):
    l = (('_none_', '_none_', '_none_'), ('fx_karo_cimg_nlmeans', 'fx_karo_cimg_nlmeans', 'fx_karo_cimg_nlmeans'), ('fx_karo_cimg_skel', 'fx_karo_cimg_skel', 'fx_karo_cimg_skel'), ('fx_karo_mm_diff', 'fx_karo_mm_diff', 'fx_karo_mm_diff'), ('fx_karo_oc_diff', 'fx_karo_oc_diff', 'fx_karo_oc_diff'), ('fx_karo_pink', 'fx_karo_pink', 'fx_karo_pink'), ('fx_karo_pink_bin', 'fx_karo_pink_bin', 'fx_karo_pink_bin'), ('fx_karo_pink_bianca', 'fx_karo_pink_bianca', 'fx_karo_pink_bianca')) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb41.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator41(bpy.types.Operator):
    bl_idname = "object.gmic_operator41"
    bl_label = "KaRo's Tests"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb41)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb41.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb42(self, context):
    l = (('fx_align_layers', 'fx_align_layers', 'fx_align_layers'), ('fx_blend_average_all', 'fx_blend_average_all', 'fx_blend_average_all'), ('fx_blend_edges', 'fx_blend_edges', 'fx_blend_edges'), ('fx_blend_fade', 'fx_blend_fade', 'fx_blend_fade'), ('fx_blend_median', 'fx_blend_median', 'fx_blend_median'), ('fx_blend_seamless', 'fx_blend_seamless', 'fx_blend_seamless'), ('fx_blend', 'fx_blend', 'fx_blend'), ('fx_split_colors', 'fx_split_colors', 'fx_split_colors'), ('fx_fade_layers', 'fx_fade_layers', 'fx_fade_layers'), ('append_tiles', 'append_tiles', 'append_tiles'), ('fx_morph_layers', 'fx_morph_layers', 'fx_morph_layers'), ('fx_apply_multiscale', 'fx_apply_multiscale', 'fx_apply_multiscale'), ('fx_pack', 'fx_pack', 'fx_pack'), ('fx_stroke', 'fx_stroke', 'fx_stroke'), ('split_tiles', 'split_tiles', 'split_tiles'), ('fx_tones2layers', 'fx_tones2layers', 'fx_tones2layers')) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb42.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator42(bpy.types.Operator):
    bl_idname = "object.gmic_operator42"
    bl_label = "Layers"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb42)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb42.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb43(self, context):
    l = (('fx_burn', 'fx_burn', 'fx_burn'), ('fx_contrast_swm', 'fx_contrast_swm', 'fx_contrast_swm'), ('fx_dodgeburn', 'fx_dodgeburn', 'fx_dodgeburn'), ('fx_drop_shadow', 'fx_drop_shadow', 'fx_drop_shadow'), ('fx_drop_shadow3d', 'fx_drop_shadow3d', 'fx_drop_shadow3d'), ('fx_equalize_shadow', 'fx_equalize_shadow', 'fx_equalize_shadow'), ('fx_illuminate_shape2d', 'fx_illuminate_shape2d', 'fx_illuminate_shape2d'), ('fx_lightglow', 'fx_lightglow', 'fx_lightglow'), ('fx_light_leaks', 'fx_light_leaks', 'fx_light_leaks'), ('fx_light_patch', 'fx_light_patch', 'fx_light_patch'), ('fx_lightrays', 'fx_lightrays', 'fx_lightrays'), ('fx_pop_shadows', 'fx_pop_shadows', 'fx_pop_shadows'), ('fx_light_relief', 'fx_light_relief', 'fx_light_relief'), ('samj_Ombre_Portee', 'samj_Ombre_Portee', 'samj_Ombre_Portee'), ('samj_Ombre_Portee_B', 'samj_Ombre_Portee_B', 'samj_Ombre_Portee_B'), ('samj_Ombre_Portee_C', 'samj_Ombre_Portee_C', 'samj_Ombre_Portee_C'), ('samj_Ombre_Portee_D', 'samj_Ombre_Portee_D', 'samj_Ombre_Portee_D'), ('fx_shadow_patch', 'fx_shadow_patch', 'fx_shadow_patch'), ('fx_slice_luminosity', 'fx_slice_luminosity', 'fx_slice_luminosity')) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb43.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator43(bpy.types.Operator):
    bl_idname = "object.gmic_operator43"
    bl_label = "Lights & Shadows"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb43)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb43.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb44(self, context):
    l = (('fx_blend_shapeaverage', 'fx_blend_shapeaverage', 'fx_blend_shapeaverage'), ('fx_lylejk_stencil', 'fx_lylejk_stencil', 'fx_lylejk_stencil'), ('Lylejk_Luma_Invert', 'Lylejk_Luma_Invert', 'Lylejk_Luma_Invert'), ('Lylejk_Quantize_Wicker', 'Lylejk_Quantize_Wicker', 'Lylejk_Quantize_Wicker'), ('Lylejk_Ribbon', 'Lylejk_Ribbon', 'Lylejk_Ribbon'), ('ripple', 'ripple', 'ripple'), ('lylejk_test_TRW', 'lylejk_test_TRW', 'lylejk_test_TRW'), ('Lylejk_Wicker', 'Lylejk_Wicker', 'Lylejk_Wicker'), ('Lylejk_Wicker_2', 'Lylejk_Wicker_2', 'Lylejk_Wicker_2'), ('Lylejk_Woven', 'Lylejk_Woven', 'Lylejk_Woven'), ('garagecoder_lylejk_samj_points_outlines', 'garagecoder_lylejk_samj_points_outlines', 'garagecoder_lylejk_samj_points_outlines')) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb44.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator44(bpy.types.Operator):
    bl_idname = "object.gmic_operator44"
    bl_label = "Lylejk"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb44)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb44.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb45(self, context):
    l = (('fx_hue_overlay_masks', 'fx_hue_overlay_masks', 'fx_hue_overlay_masks'),) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb45.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator45(bpy.types.Operator):
    bl_idname = "object.gmic_operator45"
    bl_label = "McCap"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb45)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb45.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb46(self, context):
    l = (('mc_barbed_wire', 'mc_barbed_wire', 'mc_barbed_wire'), ('mc_crosshair', 'mc_crosshair', 'mc_crosshair'), ('fx_cupid', 'fx_cupid', 'fx_cupid'), ('fx_gear', 'fx_gear', 'fx_gear'), ('fx_heart', 'fx_heart', 'fx_heart'), ('mc_paint_splat', 'mc_paint_splat', 'mc_paint_splat'), ('fx_sierpinski', 'fx_sierpinski', 'fx_sierpinski')) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb46.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator46(bpy.types.Operator):
    bl_idname = "object.gmic_operator46"
    bl_label = "Misc"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb46)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb46.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb47(self, context):
    l = (('fx_AbstractFlood', 'fx_AbstractFlood', 'fx_AbstractFlood'), ('fx_bwfilmsimulate', 'fx_bwfilmsimulate', 'fx_bwfilmsimulate'), ('fx_blockism', 'fx_blockism', 'fx_blockism'), ('fx_CompositionAnalysis', 'fx_CompositionAnalysis', 'fx_CompositionAnalysis'), ('fx_dodgesketch', 'fx_dodgesketch', 'fx_dodgesketch'), ('fx_ExposureWeightMap', 'fx_ExposureWeightMap', 'fx_ExposureWeightMap'), ('fx_StructureTensors', 'fx_StructureTensors', 'fx_StructureTensors'), ('fx_import_image_16', 'fx_import_image_16', 'fx_import_image_16'), ('fx_split_luminance', 'fx_split_luminance', 'fx_split_luminance'), ('fx_OldSquiggly', 'fx_OldSquiggly', 'fx_OldSquiggly'), ('fx_MappedSmooth', 'fx_MappedSmooth', 'fx_MappedSmooth'), ('fx_fix_HDR_black', 'fx_fix_HDR_black', 'fx_fix_HDR_black'), ('fx_noisepainting', 'fx_noisepainting', 'fx_noisepainting'), ('fx_SmoothSketch', 'fx_SmoothSketch', 'fx_SmoothSketch'), ('fx_DemoVecRot', 'fx_DemoVecRot', 'fx_DemoVecRot'), ('fx_WarpTest', 'fx_WarpTest', 'fx_WarpTest')) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb47.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator47(bpy.types.Operator):
    bl_idname = "object.gmic_operator47"
    bl_label = "Naggobot"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb47)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb47.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb48(self, context):
    l = (('mc_australia', 'mc_australia', 'mc_australia'), ('fx_barnsley_fern', 'fx_barnsley_fern', 'fx_barnsley_fern'), ('mc_gum_leaf', 'mc_gum_leaf', 'mc_gum_leaf'), ('mc_maple_leaf', 'mc_maple_leaf', 'mc_maple_leaf'), ('fx_snowflake', 'fx_snowflake', 'fx_snowflake')) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb48.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator48(bpy.types.Operator):
    bl_idname = "object.gmic_operator48"
    bl_label = "Nature"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb48)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb48.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb49(self, context):
    l = (('fx_jobs_colors', 'fx_jobs_colors', 'fx_jobs_colors'),) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb49.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator49(bpy.types.Operator):
    bl_idname = "object.gmic_operator49"
    bl_label = "Okyl168"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb49)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb49.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb50(self, context):
    l = (('fx_dragoncurve', 'fx_dragoncurve', 'fx_dragoncurve'),) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb50.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator50(bpy.types.Operator):
    bl_idname = "object.gmic_operator50"
    bl_label = "Others"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb50)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb50.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb51(self, context):
    l = (('rgb2bayer', 'rgb2bayer', 'rgb2bayer'), ('fx_boxfitting', 'fx_boxfitting', 'fx_boxfitting'), ('fx_camouflage', 'fx_camouflage', 'fx_camouflage'), ('fx_canvas', 'fx_canvas', 'fx_canvas'), ('texturize_canvas', 'texturize_canvas', 'texturize_canvas'), ('jeje_clouds', 'jeje_clouds', 'jeje_clouds'), ('fx_cracks', 'fx_cracks', 'fx_cracks'), ('fx_crystal', 'fx_crystal', 'fx_crystal'), ('fx_crystal_background', 'fx_crystal_background', 'fx_crystal_background'), ('samj_Degrades_HSL_TSL', 'samj_Degrades_HSL_TSL', 'samj_Degrades_HSL_TSL'), ('Denim_samj_en', 'Denim_samj_en', 'Denim_samj_en'), ('Denim_samj', 'Denim_samj', 'Denim_samj'), ('jeje_fibers', 'jeje_fibers', 'jeje_fibers'), ('samj_Formes_Couleurs_Variees_Dans_Image', 'samj_Formes_Couleurs_Variees_Dans_Image', 'samj_Formes_Couleurs_Variees_Dans_Image'), ('jeje_freqy_pattern', 'jeje_freqy_pattern', 'jeje_freqy_pattern'), ('fx_halftone', 'fx_halftone', 'fx_halftone'), ('fx_hearts', 'fx_hearts', 'fx_hearts'), ('fx_lava', 'fx_lava', 'fx_lava'), ('fx_marble', 'fx_marble', 'fx_marble'), ('samj_Marbre_en', 'samj_Marbre_en', 'samj_Marbre_en'), ('fx_maze', 'fx_maze', 'fx_maze'), ('fx_mineral_mosaic', 'fx_mineral_mosaic', 'fx_mineral_mosaic'), ('fx_mosaic', 'fx_mosaic', 'fx_mosaic'), ('samj_Motifs_Aleatoires_Symetriques_Degrades', 'samj_Motifs_Aleatoires_Symetriques_Degrades', 'samj_Motifs_Aleatoires_Symetriques_Degrades'), ('samj_Degrades_XYZ_CIE', 'samj_Degrades_XYZ_CIE', 'samj_Degrades_XYZ_CIE'), ('fx_shapes', 'fx_shapes', 'fx_shapes'), ('fx_pack_sprites', 'fx_pack_sprites', 'fx_pack_sprites'), ('fx_paper', 'fx_paper', 'fx_paper'), ('jeje_periodic_dots', 'jeje_periodic_dots', 'jeje_periodic_dots'), ('fx_plaid_texture', 'fx_plaid_texture', 'fx_plaid_texture'), ('samj_Points_Aleatoires_001', 'samj_Points_Aleatoires_001', 'samj_Points_Aleatoires_001'), ('fx_polka_dots', 'fx_polka_dots', 'fx_polka_dots'), ('fx_color_ellipses', 'fx_color_ellipses', 'fx_color_ellipses'), ('samj_Courtepointe', 'samj_Courtepointe', 'samj_Courtepointe'), ('samj_en_Courtepointe', 'samj_en_Courtepointe', 'samj_en_Courtepointe'), ('jeje_rays', 'jeje_rays', 'jeje_rays'), ('samj_Rays_Of_Colors', 'samj_Rays_Of_Colors', 'samj_Rays_Of_Colors'), ('syntexturize', 'syntexturize', 'syntexturize'), ('syntexturize_matchpatch', 'syntexturize_matchpatch', 'syntexturize_matchpatch'), ('fx_rorschach', 'fx_rorschach', 'fx_rorschach'), ('samj_Contours_Gros_Pixels', 'samj_Contours_Gros_Pixels', 'samj_Contours_Gros_Pixels'), ('samj_EPPE_Transform', 'samj_EPPE_Transform', 'samj_EPPE_Transform'), ('samj_Lignes_H_ou_V_Colorees', 'samj_Lignes_H_ou_V_Colorees', 'samj_Lignes_H_ou_V_Colorees'), ('samj_Marbre', 'samj_Marbre', 'samj_Marbre'), ('samj_Motif_Plasma', 'samj_Motif_Plasma', 'samj_Motif_Plasma'), ('samj_Motifs_7200', 'samj_Motifs_7200', 'samj_Motifs_7200'), ('samj_Motifs_7200_VarianteA', 'samj_Motifs_7200_VarianteA', 'samj_Motifs_7200_VarianteA'), ('samj_Motifs_7200_VarianteB', 'samj_Motifs_7200_VarianteB', 'samj_Motifs_7200_VarianteB'), ('samj_Motifs_7200_VarianteC', 'samj_Motifs_7200_VarianteC', 'samj_Motifs_7200_VarianteC'), ('samj_Steps_V2', 'samj_Steps_V2', 'samj_Steps_V2'), ('samj_Tissu_Fond_Flou', 'samj_Tissu_Fond_Flou', 'samj_Tissu_Fond_Flou'), ('samj_Variation_Stained_Glass', 'samj_Variation_Stained_Glass', 'samj_Variation_Stained_Glass'), ('fx_satin', 'fx_satin', 'fx_satin'), ('fx_mad_rorscharchp', 'fx_mad_rorscharchp', 'fx_mad_rorscharchp'), ('fx_seamless_turbulence', 'fx_seamless_turbulence', 'fx_seamless_turbulence'), ('fx_shockwaves', 'fx_shockwaves', 'fx_shockwaves'), ('samj_Soft_Random_Shades', 'samj_Soft_Random_Shades', 'samj_Soft_Random_Shades'), ('fx_sponge', 'fx_sponge', 'fx_sponge'), ('fx_stained_glass', 'fx_stained_glass', 'fx_stained_glass'), ('fx_stars', 'fx_stars', 'fx_stars'), ('fx_stencil', 'fx_stencil', 'fx_stencil'), ('samj_en_Contours_Gros_Pixels', 'samj_en_Contours_Gros_Pixels', 'samj_en_Contours_Gros_Pixels'), ('jeje_strip', 'jeje_strip', 'jeje_strip'), ('fx_tetris', 'fx_tetris', 'fx_tetris'), ('fx_truchet', 'fx_truchet', 'fx_truchet'), ('jeje_turing_pattern', 'jeje_turing_pattern', 'jeje_turing_pattern'), ('fx_voronoi', 'fx_voronoi', 'fx_voronoi'), ('weave', 'weave', 'weave'), ('fx_whirls', 'fx_whirls', 'fx_whirls')) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb51.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator51(bpy.types.Operator):
    bl_idname = "object.gmic_operator51"
    bl_label = "Patterns"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb51)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb51.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb52(self, context):
    l = (('fx_steampen', 'fx_steampen', 'fx_steampen'), ('fx_compose_boostscreen', 'fx_compose_boostscreen', 'fx_compose_boostscreen'), ('fx_compose_colordoping', 'fx_compose_colordoping', 'fx_compose_colordoping'), ('fx_colorsketchbw', 'fx_colorsketchbw', 'fx_colorsketchbw'), ('fx_colorstamp', 'fx_colorstamp', 'fx_colorstamp'), ('fx_compose_comix_color', 'fx_compose_comix_color', 'fx_compose_comix_color'), ('fx_compose_darkedges', 'fx_compose_darkedges', 'fx_compose_darkedges'), ('fx_compose_darkscreen', 'fx_compose_darkscreen', 'fx_compose_darkscreen'), ('fx_graphic_boost', 'fx_graphic_boost', 'fx_graphic_boost'), ('fx_compose_graphicolor', 'fx_compose_graphicolor', 'fx_compose_graphicolor'), ('fx_novelfx', 'fx_novelfx', 'fx_novelfx'), ('fx_compose_graphixcolor', 'fx_compose_graphixcolor', 'fx_compose_graphixcolor'), ('fx_compose_heavyscreen', 'fx_compose_heavyscreen', 'fx_compose_heavyscreen'), ('fx_metalgrain', 'fx_metalgrain', 'fx_metalgrain'), ('fx_metallicstencils', 'fx_metallicstencils', 'fx_metallicstencils'), ('fx_phoenix', 'fx_phoenix', 'fx_phoenix'), ('fx_smooth_anisotropic', 'fx_smooth_anisotropic', 'fx_smooth_anisotropic'), ('fx_psyglass', 'fx_psyglass', 'fx_psyglass'), ('fx_scaledown3', 'fx_scaledown3', 'fx_scaledown3'), ('fx_viral', 'fx_viral', 'fx_viral'), ('fx_compose_vivid_color', 'fx_compose_vivid_color', 'fx_compose_vivid_color'), ('fx_compose_vividedges', 'fx_compose_vividedges', 'fx_compose_vividedges'), ('fx_compose_vividscreen', 'fx_compose_vividscreen', 'fx_compose_vividscreen'), ('fx_m_l_unsharp2', 'fx_m_l_unsharp2', 'fx_m_l_unsharp2')) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb52.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator52(bpy.types.Operator):
    bl_idname = "object.gmic_operator52"
    bl_label = "PhotoComix"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb52)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb52.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb53(self, context):
    l = (('fx_blocks3d', 'fx_blocks3d', 'fx_blocks3d'), ('fx_coloredobject3d', 'fx_coloredobject3d', 'fx_coloredobject3d'), ('fx_elevation3d', 'fx_elevation3d', 'fx_elevation3d'), ('fx_extrude3d', 'fx_extrude3d', 'fx_extrude3d'), ('fx_imageobject3d', 'fx_imageobject3d', 'fx_imageobject3d'), ('fx_lathing3d', 'fx_lathing3d', 'fx_lathing3d'), ('fx_random3d', 'fx_random3d', 'fx_random3d'), ('samj_Adjacent_Annular_Steiner_Chains_en', 'samj_Adjacent_Annular_Steiner_Chains_en', 'samj_Adjacent_Annular_Steiner_Chains_en'), ('samj_Adjacent_Annular_Steiner_Chains', 'samj_Adjacent_Annular_Steiner_Chains', 'samj_Adjacent_Annular_Steiner_Chains'), ('samj_Rectangles_Adjacents', 'samj_Rectangles_Adjacents', 'samj_Rectangles_Adjacents'), ('samj_en_Rectangles_Adjacents', 'samj_en_Rectangles_Adjacents', 'samj_en_Rectangles_Adjacents'), ('samj_Annular_Steiner_Chains', 'samj_Annular_Steiner_Chains', 'samj_Annular_Steiner_Chains'), ('samj_en_Annular_Steiner_Chains', 'samj_en_Annular_Steiner_Chains', 'samj_en_Annular_Steiner_Chains'), ('fx_ball', 'fx_ball', 'fx_ball'), ('samj_Noel_2016', 'samj_Noel_2016', 'samj_Noel_2016'), ('samj_en_Chryzodes', 'samj_en_Chryzodes', 'samj_en_Chryzodes'), ('samj_Chryzodes', 'samj_Chryzodes', 'samj_Chryzodes'), ('fx_circle_art', 'fx_circle_art', 'fx_circle_art'), ('samj_Contour_Line_Laser_LED', 'samj_Contour_Line_Laser_LED', 'samj_Contour_Line_Laser_LED'), ('fx_crazy_texture', 'fx_crazy_texture', 'fx_crazy_texture'), ('samj_dessiner_un_polygone', 'samj_dessiner_un_polygone', 'samj_dessiner_un_polygone'), ('samj_Egg_Oeuf_Granville', 'samj_Egg_Oeuf_Granville', 'samj_Egg_Oeuf_Granville'), ('samj_Egg_Oeuf_Hugelschaffer', 'samj_Egg_Oeuf_Hugelschaffer', 'samj_Egg_Oeuf_Hugelschaffer'), ('samj_Egg_Oeuf_Rosillo', 'samj_Egg_Oeuf_Rosillo', 'samj_Egg_Oeuf_Rosillo'), ('samj_Engrenages_Laser_LED', 'samj_Engrenages_Laser_LED', 'samj_Engrenages_Laser_LED'), ('fx_equation_parametric', 'fx_equation_parametric', 'fx_equation_parametric'), ('fx_equation_plot', 'fx_equation_plot', 'fx_equation_plot'), ('samj_Etoile_De_Pompei_Triangles_Sierpinski', 'samj_Etoile_De_Pompei_Triangles_Sierpinski', 'samj_Etoile_De_Pompei_Triangles_Sierpinski'), ('samj_Etoiles_Laser_LED', 'samj_Etoiles_Laser_LED', 'samj_Etoiles_Laser_LED'), ('samj_Etoiles_Remplies_Triangles_Sierpinski', 'samj_Etoiles_Remplies_Triangles_Sierpinski', 'samj_Etoiles_Remplies_Triangles_Sierpinski'), ('samj_Flocon_De_Neige', 'samj_Flocon_De_Neige', 'samj_Flocon_De_Neige'), ('samj_Flocon_Laser_LED', 'samj_Flocon_Laser_LED', 'samj_Flocon_Laser_LED'), ('samj_Fractal_Tree', 'samj_Fractal_Tree', 'samj_Fractal_Tree'), ('fx_corner_gradient', 'fx_corner_gradient', 'fx_corner_gradient'), ('fx_custom_gradient', 'fx_custom_gradient', 'fx_custom_gradient'), ('fx_line_gradient', 'fx_line_gradient', 'fx_line_gradient'), ('fx_linear_gradient', 'fx_linear_gradient', 'fx_linear_gradient'), ('fx_radial_gradient', 'fx_radial_gradient', 'fx_radial_gradient'), ('fx_random_gradient', 'fx_random_gradient', 'fx_random_gradient'), ('samj_Linear_Gradient_CIE_Lab', 'samj_Linear_Gradient_CIE_Lab', 'samj_Linear_Gradient_CIE_Lab'), ('samj_en_Linear_Gradient_CIE_Lab', 'samj_en_Linear_Gradient_CIE_Lab', 'samj_en_Linear_Gradient_CIE_Lab'), ('samj_en_Shape_Linear_Gradient_CIE_Lab', 'samj_en_Shape_Linear_Gradient_CIE_Lab', 'samj_en_Shape_Linear_Gradient_CIE_Lab'), ('samj_Shape_Linear_Gradient_CIE_Lab', 'samj_Shape_Linear_Gradient_CIE_Lab', 'samj_Shape_Linear_Gradient_CIE_Lab'), ('gtutor_hairlock', 'gtutor_hairlock', 'gtutor_hairlock'), ('Harmonograph_samj_en', 'Harmonograph_samj_en', 'Harmonograph_samj_en'), ('Harmonograph_samj', 'Harmonograph_samj', 'Harmonograph_samj'), ('samj_Hawaiian_Earring', 'samj_Hawaiian_Earring', 'samj_Hawaiian_Earring'), ('samj_en_Hawaiian_Earring', 'samj_en_Hawaiian_Earring', 'samj_en_Hawaiian_Earring'), ('fx_lightning', 'fx_lightning', 'fx_lightning'), ('Traits_Strokes_samj_en', 'Traits_Strokes_samj_en', 'Traits_Strokes_samj_en'), ('samj_en_Lignes_Epaisseur_Variable', 'samj_en_Lignes_Epaisseur_Variable', 'samj_en_Lignes_Epaisseur_Variable'), ('samj_Lignes_Epaisseur_Variable', 'samj_Lignes_Epaisseur_Variable', 'samj_Lignes_Epaisseur_Variable'), ('fx_lissajous', 'fx_lissajous', 'fx_lissajous'), ('fx_mandelbrot', 'fx_mandelbrot', 'fx_mandelbrot'), ('fx_neon_lightning', 'fx_neon_lightning', 'fx_neon_lightning'), ('fx_newton_fractal', 'fx_newton_fractal', 'fx_newton_fractal'), ('samj_Orbites', 'samj_Orbites', 'samj_Orbites'), ('samj_en_Cercles_Tangents_Dans_Cercle', 'samj_en_Cercles_Tangents_Dans_Cercle', 'samj_en_Cercles_Tangents_Dans_Cercle'), ('samj_Cercles_Tangents_Dans_Cercle', 'samj_Cercles_Tangents_Dans_Cercle', 'samj_Cercles_Tangents_Dans_Cercle'), ('Pintograph_samj_en', 'Pintograph_samj_en', 'Pintograph_samj_en'), ('Pintograph_samj', 'Pintograph_samj', 'Pintograph_samj'), ('fx_plasma', 'fx_plasma', 'fx_plasma'), ('samj_Poisson_D_Avril', 'samj_Poisson_D_Avril', 'samj_Poisson_D_Avril'), ('samj_Arbre_Pythagore', 'samj_Arbre_Pythagore', 'samj_Arbre_Pythagore'), ('fx_quick_copyright', 'fx_quick_copyright', 'fx_quick_copyright'), ('fx_rainbow', 'fx_rainbow', 'fx_rainbow'), ('fx_rectexture', 'fx_rectexture', 'fx_rectexture'), ('samj_Rosace_Triangles_Sierpinski', 'samj_Rosace_Triangles_Sierpinski', 'samj_Rosace_Triangles_Sierpinski'), ('samj_en_Cercles_Qui_Tournent', 'samj_en_Cercles_Qui_Tournent', 'samj_en_Cercles_Qui_Tournent'), ('samj_Cercles_Qui_Tournent', 'samj_Cercles_Qui_Tournent', 'samj_Cercles_Qui_Tournent'), ('samj_Chains_Solidify', 'samj_Chains_Solidify', 'samj_Chains_Solidify'), ('samj_Palette_De_Degrades', 'samj_Palette_De_Degrades', 'samj_Palette_De_Degrades'), ('samj_Splines_Test', 'samj_Splines_Test', 'samj_Splines_Test'), ('samj_Test_Visu_3D', 'samj_Test_Visu_3D', 'samj_Test_Visu_3D'), ('fx_shadebobs', 'fx_shadebobs', 'fx_shadebobs'), ('samj_Formes_Geometriques_Simples', 'samj_Formes_Geometriques_Simples', 'samj_Formes_Geometriques_Simples'), ('samj_en_Formes_Geometriques_Simples', 'samj_en_Formes_Geometriques_Simples', 'samj_en_Formes_Geometriques_Simples'), ('samj_en_Flocon_De_Neige', 'samj_en_Flocon_De_Neige', 'samj_en_Flocon_De_Neige'), ('Spirographe_samj_en', 'Spirographe_samj_en', 'Spirographe_samj_en'), ('Spirographe_samj', 'Spirographe_samj', 'Spirographe_samj'), ('samj_Des_Lignes_002', 'samj_Des_Lignes_002', 'samj_Des_Lignes_002'), ('samj_en_Des_Lignes_002', 'samj_en_Des_Lignes_002', 'samj_en_Des_Lignes_002'), ('fx_superformula', 'fx_superformula', 'fx_superformula'), ('samj_Superposition_Triangles_Sierpinski', 'samj_Superposition_Triangles_Sierpinski', 'samj_Superposition_Triangles_Sierpinski'), ('fx_symmetric_shape2d', 'fx_symmetric_shape2d', 'fx_symmetric_shape2d'), ('Traits_Strokes_samj', 'Traits_Strokes_samj', 'Traits_Strokes_samj'), ('fx_tree', 'fx_tree', 'fx_tree'), ('Triangles_Shades_Adjacents', 'Triangles_Shades_Adjacents', 'Triangles_Shades_Adjacents'), ('fx_turbulence', 'fx_turbulence', 'fx_turbulence'), ('Twisted_Rays_en', 'Twisted_Rays_en', 'Twisted_Rays_en'), ('Twisted_Rays', 'Twisted_Rays', 'Twisted_Rays')) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb53.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator53(bpy.types.Operator):
    bl_idname = "object.gmic_operator53"
    bl_label = "Rendering"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb53)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb53.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb54(self, context):
    l = (('banding_denoise', 'banding_denoise', 'banding_denoise'), ('bayer2rgb', 'bayer2rgb', 'bayer2rgb'), ('afre_cleantext', 'afre_cleantext', 'afre_cleantext'), ('deinterlace', 'deinterlace', 'deinterlace'), ('gcd_deinterlace2x', 'gcd_deinterlace2x', 'gcd_deinterlace2x'), ('fx_pahlsson_descreen', 'fx_pahlsson_descreen', 'fx_pahlsson_descreen'), ('gcd_despeckle', 'gcd_despeckle', 'gcd_despeckle'), ('iain_nr_2019', 'iain_nr_2019', 'iain_nr_2019'), ('iain_fast_denoise_p', 'iain_fast_denoise_p', 'iain_fast_denoise_p'), ('fx_inpaint_holes', 'fx_inpaint_holes', 'fx_inpaint_holes'), ('fx_inpaint_morpho', 'fx_inpaint_morpho', 'fx_inpaint_morpho'), ('fx_inpaint_matchpatch', 'fx_inpaint_matchpatch', 'fx_inpaint_matchpatch'), ('fx_inpaint_patch', 'fx_inpaint_patch', 'fx_inpaint_patch'), ('fx_inpaint_pde', 'fx_inpaint_pde', 'fx_inpaint_pde'), ('local_similarity_mask', 'local_similarity_mask', 'local_similarity_mask'), ('iain_pixel_denoise_p', 'iain_pixel_denoise_p', 'iain_pixel_denoise_p'), ('iain_recursive_median_p', 'iain_recursive_median_p', 'iain_recursive_median_p'), ('red_eye', 'red_eye', 'red_eye'), ('fx_remove_hotpixels', 'fx_remove_hotpixels', 'fx_remove_hotpixels'), ('jeje_scandoc', 'jeje_scandoc', 'jeje_scandoc'), ('samj_CorLine', 'samj_CorLine', 'samj_CorLine'), ('samj_CorLine_B', 'samj_CorLine_B', 'samj_CorLine_B'), ('fx_smooth_anisotropic', 'fx_smooth_anisotropic', 'fx_smooth_anisotropic'), ('fx_smooth_antialias', 'fx_smooth_antialias', 'fx_smooth_antialias'), ('fx_smooth_bilateral', 'fx_smooth_bilateral', 'fx_smooth_bilateral'), ('jeje_denoise_patch_dict', 'jeje_denoise_patch_dict', 'jeje_denoise_patch_dict'), ('fx_smooth_diffusion', 'fx_smooth_diffusion', 'fx_smooth_diffusion'), ('fx_smooth_guided', 'fx_smooth_guided', 'fx_smooth_guided'), ('jeje_denoise_iuwt', 'jeje_denoise_iuwt', 'jeje_denoise_iuwt'), ('fx_smooth_meancurvature', 'fx_smooth_meancurvature', 'fx_smooth_meancurvature'), ('fx_smooth_median', 'fx_smooth_median', 'fx_smooth_median'), ('fx_smooth_nlmeans', 'fx_smooth_nlmeans', 'fx_smooth_nlmeans'), ('fx_smooth_patch', 'fx_smooth_patch', 'fx_smooth_patch'), ('fx_smooth_patchpca', 'fx_smooth_patchpca', 'fx_smooth_patchpca'), ('fx_smooth_peronamalik', 'fx_smooth_peronamalik', 'fx_smooth_peronamalik'), ('fx_smooth_selective', 'fx_smooth_selective', 'fx_smooth_selective'), ('fx_smooth_skin', 'fx_smooth_skin', 'fx_smooth_skin'), ('fx_smooth_anisotropic', 'fx_smooth_anisotropic', 'fx_smooth_anisotropic'), ('fx_smooth_tv', 'fx_smooth_tv', 'fx_smooth_tv'), ('fx_smooth_haar', 'fx_smooth_haar', 'fx_smooth_haar'), ('jeje_local_wiener', 'jeje_local_wiener', 'jeje_local_wiener'), ('fx_solidify_td', 'fx_solidify_td', 'fx_solidify_td'), ('unpurple', 'unpurple', 'unpurple'), ('jeje_unstrip', 'jeje_unstrip', 'jeje_unstrip'), ('fx_scale_dcci2x', 'fx_scale_dcci2x', 'fx_scale_dcci2x'), ('fx_upscale_smart', 'fx_upscale_smart', 'fx_upscale_smart'), ('fx_scalenx', 'fx_scalenx', 'fx_scalenx')) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb54.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator54(bpy.types.Operator):
    bl_idname = "object.gmic_operator54"
    bl_label = "Repair"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb54)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb54.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb55(self, context):
    l = (('fx_rep_trsa', 'fx_rep_trsa', 'fx_rep_trsa'), ('gui_rep_acb', 'gui_rep_acb', 'gui_rep_acb'), ('gui_axis_streak', 'gui_axis_streak', 'gui_axis_streak'), ('rep_binary_quaddro_basic_gui', 'rep_binary_quaddro_basic_gui', 'rep_binary_quaddro_basic_gui'), ('rep_binary_quaddro_mc_gui', 'rep_binary_quaddro_mc_gui', 'rep_binary_quaddro_mc_gui'), ('gui_rep_shape_brick', 'gui_rep_shape_brick', 'gui_rep_shape_brick'), ('fx_OOBS', 'fx_OOBS', 'fx_OOBS'), ('rep_color_existence_distribution_rgb8', 'rep_color_existence_distribution_rgb8', 'rep_color_existence_distribution_rgb8'), ('gui_rep_colmt', 'gui_rep_colmt', 'gui_rep_colmt'), ('_cons_turb', '_cons_turb', '_cons_turb'), ('fx_emboss_relief', 'fx_emboss_relief', 'fx_emboss_relief'), ('gui_rep_fibo', 'gui_rep_fibo', 'gui_rep_fibo'), ('gui_rep_frblur', 'gui_rep_frblur', 'gui_rep_frblur'), ('gui_rep_gv', 'gui_rep_gv', 'gui_rep_gv'), ('goof_res', 'goof_res', 'goof_res'), ('gui_rep_regm', 'gui_rep_regm', 'gui_rep_regm'), ('fx_rep_graduated_filter', 'fx_rep_graduated_filter', 'fx_rep_graduated_filter'), ('fx_rep_sptbwgp', 'fx_rep_sptbwgp', 'fx_rep_sptbwgp'), ('gui_rep_sptbwgp_recpoltrans', 'gui_rep_sptbwgp_recpoltrans', 'gui_rep_sptbwgp_recpoltrans'), ('gui_rep_polkal', 'gui_rep_polkal', 'gui_rep_polkal'), ('rep_logpindis_gui', 'rep_logpindis_gui', 'rep_logpindis_gui'), ('gui_rep_majority', 'gui_rep_majority', 'gui_rep_majority'), ('gui_rep_majority_threshold', 'gui_rep_majority_threshold', 'gui_rep_majority_threshold'), ('fx_modulo', 'fx_modulo', 'fx_modulo'), ('fx_modulo', 'fx_modulo', 'fx_modulo'), ('fx_rep_nebulous', 'fx_rep_nebulous', 'fx_rep_nebulous'), ('rep_mj_newf', 'rep_mj_newf', 'rep_mj_newf'), ('fx_ncee', 'fx_ncee', 'fx_ncee'), ('fx_rep_rpgtiler_noniso', 'fx_rep_rpgtiler_noniso', 'fx_rep_rpgtiler_noniso'), ('gui_rep_objvf', 'gui_rep_objvf', 'gui_rep_objvf'), ('fx_rep_loupasc_ordered_dither', 'fx_rep_loupasc_ordered_dither', 'fx_rep_loupasc_ordered_dither'), ('gui_rep_perspective_streak', 'gui_rep_perspective_streak', 'gui_rep_perspective_streak'), ('fx_rep_photomosaic', 'fx_rep_photomosaic', 'fx_rep_photomosaic'), ('fx_rep_pxpush', 'fx_rep_pxpush', 'fx_rep_pxpush'), ('gui_rep_pw', 'gui_rep_pw', 'gui_rep_pw'), ('palgen', 'palgen', 'palgen'), ('gui_rep_prime_surface', 'gui_rep_prime_surface', 'gui_rep_prime_surface'), ('fx_rep_rand_sqrrecfill', 'fx_rep_rand_sqrrecfill', 'fx_rep_rand_sqrrecfill'), ('fx_rep_lerp_rgb_gray', 'fx_rep_lerp_rgb_gray', 'fx_rep_lerp_rgb_gray'), ('fx_rep_rbtt', 'fx_rep_rbtt', 'fx_rep_rbtt'), ('rep_sinowaterdist_gui', 'rep_sinowaterdist_gui', 'rep_sinowaterdist_gui'), ('gui_rep_sd', 'gui_rep_sd', 'gui_rep_sd'), ('rep_sqrlogpindis_gui', 'rep_sqrlogpindis_gui', 'rep_sqrlogpindis_gui'), ('rep_stitch_gui', 'rep_stitch_gui', 'rep_stitch_gui'), ('rep_strbul', 'rep_strbul', 'rep_strbul'), ('rep_strbulkal_gui', 'rep_strbulkal_gui', 'rep_strbulkal_gui'), ('gui_rep_tfrac', 'gui_rep_tfrac', 'gui_rep_tfrac'), ('gui_rep_form_pixel', 'gui_rep_form_pixel', 'gui_rep_form_pixel'), ('gui_rep_trif', 'gui_rep_trif', 'gui_rep_trif'), ('gui_rep_trps', 'gui_rep_trps', 'gui_rep_trps'), ('tcrc', 'tcrc', 'tcrc'), ('fx_rep_tg3', 'fx_rep_tg3', 'fx_rep_tg3'), ('fx_vibrato', 'fx_vibrato', 'fx_vibrato'), ('rep_z_render', 'rep_z_render', 'rep_z_render')) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb55.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator55(bpy.types.Operator):
    bl_idname = "object.gmic_operator55"
    bl_label = "Reptorian"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb55)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb55.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb56(self, context):
    l = (('plasma_transition', 'plasma_transition', 'plasma_transition'), ('randomwaves', 'randomwaves', 'randomwaves')) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb56.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator56(bpy.types.Operator):
    bl_idname = "object.gmic_operator56"
    bl_label = "RL"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb56)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb56.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb57(self, context):
    l = (('fx_adjust_orientation', 'fx_adjust_orientation', 'fx_adjust_orientation'), ('fx_apply_curve', 'fx_apply_curve', 'fx_apply_curve'), ('fx_faded_mirror', 'fx_faded_mirror', 'fx_faded_mirror'), ('gaap_test', 'gaap_test', 'gaap_test'), ('fx_gca', 'fx_gca', 'fx_gca'), ('fx_grain', 'fx_grain', 'fx_grain'), ('fx_krita', 'fx_krita', 'fx_krita'), ('gui_layer_info', 'gui_layer_info', 'gui_layer_info'), ('fx_perspective_scale', 'fx_perspective_scale', 'fx_perspective_scale'), ('dt_segment_shaded', 'dt_segment_shaded', 'dt_segment_shaded')) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb57.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator57(bpy.types.Operator):
    bl_idname = "object.gmic_operator57"
    bl_label = "Ronounours"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb57)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb57.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb58(self, context):
    l = (('_none_', '_none_', '_none_'),) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb58.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator58(bpy.types.Operator):
    bl_idname = "object.gmic_operator58"
    bl_label = "Samj"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb58)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb58.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb59(self, context):
    l = (('fx_animate_elevation3d', 'fx_animate_elevation3d', 'fx_animate_elevation3d'), ('fx_animate_extrude3d', 'fx_animate_extrude3d', 'fx_animate_extrude3d'), ('fx_animate_imageobject3d', 'fx_animate_imageobject3d', 'fx_animate_imageobject3d'), ('fx_text_pointcloud3d', 'fx_text_pointcloud3d', 'fx_text_pointcloud3d'), ('fx_transition3d', 'fx_transition3d', 'fx_transition3d'), ('fx_animate_pencilbw', 'fx_animate_pencilbw', 'fx_animate_pencilbw'), ('fx_animate_stencilbw', 'fx_animate_stencilbw', 'fx_animate_stencilbw'), ('fx_animate_cartoon', 'fx_animate_cartoon', 'fx_animate_cartoon'), ('fx_animate_edges', 'fx_animate_edges', 'fx_animate_edges'), ('fx_fire_edges', 'fx_fire_edges', 'fx_fire_edges'), ('fx_lavalampbw', 'fx_lavalampbw', 'fx_lavalampbw'), ('fx_animate_lissajous', 'fx_animate_lissajous', 'fx_animate_lissajous'), ('fx_moire', 'fx_moire', 'fx_moire'), ('fx_tk_animateobject', 'fx_tk_animateobject', 'fx_tk_animateobject'), ('fx_animate_rodilius', 'fx_animate_rodilius', 'fx_animate_rodilius'), ('fx_animate_glow', 'fx_animate_glow', 'fx_animate_glow'), ('fx_spatial_transition', 'fx_spatial_transition', 'fx_spatial_transition')) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb59.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator59(bpy.types.Operator):
    bl_idname = "object.gmic_operator59"
    bl_label = "Sequences"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb59)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb59.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb60(self, context):
    l = (('disco', 'disco', 'disco'), ('KittyRings', 'KittyRings', 'KittyRings'), ('moon2panorama', 'moon2panorama', 'moon2panorama'), ('fx_souphead_filter', 'fx_souphead_filter', 'fx_souphead_filter'), ('spiral_RGB', 'spiral_RGB', 'spiral_RGB')) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb60.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator60(bpy.types.Operator):
    bl_idname = "object.gmic_operator60"
    bl_label = "Souphead"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb60)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb60.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb61(self, context):
    l = (('fx_tk_make3D', 'fx_tk_make3D', 'fx_tk_make3D'), ('fx_tk_video3D', 'fx_tk_video3D', 'fx_tk_video3D'), ('fx_tk_autodepth', 'fx_tk_autodepth', 'fx_tk_autodepth'), ('fx_tk_deana', 'fx_tk_deana', 'fx_tk_deana'), ('fx_tk_depthmap', 'fx_tk_depthmap', 'fx_tk_depthmap'), ('fx_tk_depth_obtain', 'fx_tk_depth_obtain', 'fx_tk_depth_obtain'), ('fx_tk_lenticular', 'fx_tk_lenticular', 'fx_tk_lenticular'), ('fx_tk_stereogram', 'fx_tk_stereogram', 'fx_tk_stereogram'), ('gcd_stereo_img', 'gcd_stereo_img', 'gcd_stereo_img'), ('fx_tk_stereoimage', 'fx_tk_stereoimage', 'fx_tk_stereoimage'), ('gcd_unstereo', 'gcd_unstereo', 'gcd_unstereo')) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb61.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator61(bpy.types.Operator):
    bl_idname = "object.gmic_operator61"
    bl_label = "Stereoscopic 3D"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb61)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb61.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb62(self, context):
    l = (('mc_flou', 'mc_flou', 'mc_flou'), ('mc_pendraw', 'mc_pendraw', 'mc_pendraw')) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb62.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator62(bpy.types.Operator):
    bl_idname = "object.gmic_operator62"
    bl_label = "Telperion"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb62)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb62.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb63(self, context):
    l = (('_none_', '_none_', '_none_'), ('fx_tk_retouch', 'fx_tk_retouch', 'fx_tk_retouch'), ('fx_tk_dof', 'fx_tk_dof', 'fx_tk_dof'), ('fx_tk_infrared', 'fx_tk_infrared', 'fx_tk_infrared')) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb63.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator63(bpy.types.Operator):
    bl_idname = "object.gmic_operator63"
    bl_label = "Tom Keil"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb63)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb63.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb64(self, context):
    l = (('samj_CeKoaSa_001', 'samj_CeKoaSa_001', 'samj_CeKoaSa_001'), ('samj_CeKoaSa_002', 'samj_CeKoaSa_002', 'samj_CeKoaSa_002'), ('samj_CeKoaSa_003', 'samj_CeKoaSa_003', 'samj_CeKoaSa_003'), ('samj_CeKoaSa_004', 'samj_CeKoaSa_004', 'samj_CeKoaSa_004'), ('samj_CeKoaSa_005', 'samj_CeKoaSa_005', 'samj_CeKoaSa_005'), ('fx_custom_code', 'fx_custom_code', 'fx_custom_code'), ('fx_custom_code', 'fx_custom_code', 'fx_custom_code'), ('Je_passe_l_hiver_en_Floride', 'Je_passe_l_hiver_en_Floride', 'Je_passe_l_hiver_en_Floride'), ('fx_output_565', 'fx_output_565', 'fx_output_565'), ('fx_gmic_demos', 'fx_gmic_demos', 'fx_gmic_demos'), ('_none_', '_none_', '_none_'), ('fx_import_image', 'fx_import_image', 'fx_import_image'), ('fx_input_565', 'fx_input_565', 'fx_input_565'), ('fx_intarsia', 'fx_intarsia', 'fx_intarsia'), ('Polygonize_GUI', 'Polygonize_GUI', 'Polygonize_GUI'), ('gimp_recolorize_20130115_modifie', 'gimp_recolorize_20130115_modifie', 'gimp_recolorize_20130115_modifie'), ('samj_BoxFiter_Map', 'samj_BoxFiter_Map', 'samj_BoxFiter_Map'), ('samj_BoxFiter_Test', 'samj_BoxFiter_Test', 'samj_BoxFiter_Test'), ('samj_CeKoaSa_007', 'samj_CeKoaSa_007', 'samj_CeKoaSa_007'), ('samj_CeKoaSa_008', 'samj_CeKoaSa_008', 'samj_CeKoaSa_008'), ('samj_CeKoaSa_009', 'samj_CeKoaSa_009', 'samj_CeKoaSa_009'), ('samj_CeKoaSa_010', 'samj_CeKoaSa_010', 'samj_CeKoaSa_010'), ('samj_CeKoaSa_011', 'samj_CeKoaSa_011', 'samj_CeKoaSa_011'), ('samj_Relief_A', 'samj_Relief_A', 'samj_Relief_A'), ('samj_test_A', 'samj_test_A', 'samj_test_A'), ('samj_test_B', 'samj_test_B', 'samj_test_B'), ('samj_test_C', 'samj_test_C', 'samj_test_C'), ('samj_test_D', 'samj_test_D', 'samj_test_D'), ('samj_test_Dither_Color', 'samj_test_Dither_Color', 'samj_test_Dither_Color'), ('samj_test_E', 'samj_test_E', 'samj_test_E'), ('samj_test_F', 'samj_test_F', 'samj_test_F'), ('samj_test_G', 'samj_test_G', 'samj_test_G'), ('samj_Test_Solidify', 'samj_Test_Solidify', 'samj_Test_Solidify'), ('fx_image_sample', 'fx_image_sample', 'fx_image_sample'), ('fx_solve_maze', 'fx_solve_maze', 'fx_solve_maze'), ('samj_test_x_color_curves', 'samj_test_x_color_curves', 'samj_test_x_color_curves'), ('samj_gimp_texture_zero_zero_deux', 'samj_gimp_texture_zero_zero_deux', 'samj_gimp_texture_zero_zero_deux'), ('samj_Texture_Aquarelle_1', 'samj_Texture_Aquarelle_1', 'samj_Texture_Aquarelle_1'), ('samj_Toile_D_Araignee', 'samj_Toile_D_Araignee', 'samj_Toile_D_Araignee'), ('samj_test_tout_interactif', 'samj_test_tout_interactif', 'samj_test_tout_interactif')) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb64.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator64(bpy.types.Operator):
    bl_idname = "object.gmic_operator64"
    bl_label = "Various"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb64)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb64.lookup[self.myprop])
        return {'FINISHED'}


def gmic_enum_items_cb65(self, context):
    l = (('demo_ra', 'demo_ra', 'demo_ra'), ('demo_xy', 'demo_xy', 'demo_xy'), ('fx_fourier_picture_watermark', 'fx_fourier_picture_watermark', 'fx_fourier_picture_watermark'), ('mathmap_flag', 'mathmap_flag', 'mathmap_flag'), ('mathmap_rel2ellv3', 'mathmap_rel2ellv3', 'mathmap_rel2ellv3'), ('mathmap_spiral', 'mathmap_spiral', 'mathmap_spiral')) #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb65.lookup = {id: name for id, name, desc in l}
    return l

class GmicOperator65(bpy.types.Operator):
    bl_idname = "object.gmic_operator65"
    bl_label = "Zonderr"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb65)

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({'INFO'}, gmic_enum_items_cb65.lookup[self.myprop])
        return {'FINISHED'}


class SimpleCustomMenu(bpy.types.Menu):
    bl_label = "G'MIC Quick Filters"
    bl_idname = "OBJECT_MT_simple_custom_menu"

    def draw(self, context):
        layout = self.layout
        op = layout.operator_menu_enum(GmicOperator0.bl_idname, 'myprop', text=GmicOperator0.bl_label)
        op = layout.operator_menu_enum(GmicOperator1.bl_idname, 'myprop', text=GmicOperator1.bl_label)
        op = layout.operator_menu_enum(GmicOperator2.bl_idname, 'myprop', text=GmicOperator2.bl_label)
        op = layout.operator_menu_enum(GmicOperator3.bl_idname, 'myprop', text=GmicOperator3.bl_label)
        op = layout.operator_menu_enum(GmicOperator4.bl_idname, 'myprop', text=GmicOperator4.bl_label)
        op = layout.operator_menu_enum(GmicOperator5.bl_idname, 'myprop', text=GmicOperator5.bl_label)
        op = layout.operator_menu_enum(GmicOperator6.bl_idname, 'myprop', text=GmicOperator6.bl_label)
        op = layout.operator_menu_enum(GmicOperator7.bl_idname, 'myprop', text=GmicOperator7.bl_label)
        op = layout.operator_menu_enum(GmicOperator8.bl_idname, 'myprop', text=GmicOperator8.bl_label)
        op = layout.operator_menu_enum(GmicOperator9.bl_idname, 'myprop', text=GmicOperator9.bl_label)
        op = layout.operator_menu_enum(GmicOperator10.bl_idname, 'myprop', text=GmicOperator10.bl_label)
        op = layout.operator_menu_enum(GmicOperator11.bl_idname, 'myprop', text=GmicOperator11.bl_label)
        op = layout.operator_menu_enum(GmicOperator12.bl_idname, 'myprop', text=GmicOperator12.bl_label)
        op = layout.operator_menu_enum(GmicOperator13.bl_idname, 'myprop', text=GmicOperator13.bl_label)
        op = layout.operator_menu_enum(GmicOperator14.bl_idname, 'myprop', text=GmicOperator14.bl_label)
        op = layout.operator_menu_enum(GmicOperator15.bl_idname, 'myprop', text=GmicOperator15.bl_label)
        op = layout.operator_menu_enum(GmicOperator16.bl_idname, 'myprop', text=GmicOperator16.bl_label)
        op = layout.operator_menu_enum(GmicOperator17.bl_idname, 'myprop', text=GmicOperator17.bl_label)
        op = layout.operator_menu_enum(GmicOperator18.bl_idname, 'myprop', text=GmicOperator18.bl_label)
        op = layout.operator_menu_enum(GmicOperator19.bl_idname, 'myprop', text=GmicOperator19.bl_label)
        op = layout.operator_menu_enum(GmicOperator20.bl_idname, 'myprop', text=GmicOperator20.bl_label)
        op = layout.operator_menu_enum(GmicOperator21.bl_idname, 'myprop', text=GmicOperator21.bl_label)
        op = layout.operator_menu_enum(GmicOperator22.bl_idname, 'myprop', text=GmicOperator22.bl_label)
        op = layout.operator_menu_enum(GmicOperator23.bl_idname, 'myprop', text=GmicOperator23.bl_label)
        op = layout.operator_menu_enum(GmicOperator24.bl_idname, 'myprop', text=GmicOperator24.bl_label)
        op = layout.operator_menu_enum(GmicOperator25.bl_idname, 'myprop', text=GmicOperator25.bl_label)
        op = layout.operator_menu_enum(GmicOperator26.bl_idname, 'myprop', text=GmicOperator26.bl_label)
        op = layout.operator_menu_enum(GmicOperator27.bl_idname, 'myprop', text=GmicOperator27.bl_label)
        op = layout.operator_menu_enum(GmicOperator28.bl_idname, 'myprop', text=GmicOperator28.bl_label)
        op = layout.operator_menu_enum(GmicOperator29.bl_idname, 'myprop', text=GmicOperator29.bl_label)
        op = layout.operator_menu_enum(GmicOperator30.bl_idname, 'myprop', text=GmicOperator30.bl_label)
        op = layout.operator_menu_enum(GmicOperator31.bl_idname, 'myprop', text=GmicOperator31.bl_label)
        op = layout.operator_menu_enum(GmicOperator32.bl_idname, 'myprop', text=GmicOperator32.bl_label)
        op = layout.operator_menu_enum(GmicOperator33.bl_idname, 'myprop', text=GmicOperator33.bl_label)
        op = layout.operator_menu_enum(GmicOperator34.bl_idname, 'myprop', text=GmicOperator34.bl_label)
        op = layout.operator_menu_enum(GmicOperator35.bl_idname, 'myprop', text=GmicOperator35.bl_label)
        op = layout.operator_menu_enum(GmicOperator36.bl_idname, 'myprop', text=GmicOperator36.bl_label)
        op = layout.operator_menu_enum(GmicOperator37.bl_idname, 'myprop', text=GmicOperator37.bl_label)
        op = layout.operator_menu_enum(GmicOperator38.bl_idname, 'myprop', text=GmicOperator38.bl_label)
        op = layout.operator_menu_enum(GmicOperator39.bl_idname, 'myprop', text=GmicOperator39.bl_label)
        op = layout.operator_menu_enum(GmicOperator40.bl_idname, 'myprop', text=GmicOperator40.bl_label)
        op = layout.operator_menu_enum(GmicOperator41.bl_idname, 'myprop', text=GmicOperator41.bl_label)
        op = layout.operator_menu_enum(GmicOperator42.bl_idname, 'myprop', text=GmicOperator42.bl_label)
        op = layout.operator_menu_enum(GmicOperator43.bl_idname, 'myprop', text=GmicOperator43.bl_label)
        op = layout.operator_menu_enum(GmicOperator44.bl_idname, 'myprop', text=GmicOperator44.bl_label)
        op = layout.operator_menu_enum(GmicOperator45.bl_idname, 'myprop', text=GmicOperator45.bl_label)
        op = layout.operator_menu_enum(GmicOperator46.bl_idname, 'myprop', text=GmicOperator46.bl_label)
        op = layout.operator_menu_enum(GmicOperator47.bl_idname, 'myprop', text=GmicOperator47.bl_label)
        op = layout.operator_menu_enum(GmicOperator48.bl_idname, 'myprop', text=GmicOperator48.bl_label)
        op = layout.operator_menu_enum(GmicOperator49.bl_idname, 'myprop', text=GmicOperator49.bl_label)
        op = layout.operator_menu_enum(GmicOperator50.bl_idname, 'myprop', text=GmicOperator50.bl_label)
        op = layout.operator_menu_enum(GmicOperator51.bl_idname, 'myprop', text=GmicOperator51.bl_label)
        op = layout.operator_menu_enum(GmicOperator52.bl_idname, 'myprop', text=GmicOperator52.bl_label)
        op = layout.operator_menu_enum(GmicOperator53.bl_idname, 'myprop', text=GmicOperator53.bl_label)
        op = layout.operator_menu_enum(GmicOperator54.bl_idname, 'myprop', text=GmicOperator54.bl_label)
        op = layout.operator_menu_enum(GmicOperator55.bl_idname, 'myprop', text=GmicOperator55.bl_label)
        op = layout.operator_menu_enum(GmicOperator56.bl_idname, 'myprop', text=GmicOperator56.bl_label)
        op = layout.operator_menu_enum(GmicOperator57.bl_idname, 'myprop', text=GmicOperator57.bl_label)
        op = layout.operator_menu_enum(GmicOperator58.bl_idname, 'myprop', text=GmicOperator58.bl_label)
        op = layout.operator_menu_enum(GmicOperator59.bl_idname, 'myprop', text=GmicOperator59.bl_label)
        op = layout.operator_menu_enum(GmicOperator60.bl_idname, 'myprop', text=GmicOperator60.bl_label)
        op = layout.operator_menu_enum(GmicOperator61.bl_idname, 'myprop', text=GmicOperator61.bl_label)
        op = layout.operator_menu_enum(GmicOperator62.bl_idname, 'myprop', text=GmicOperator62.bl_label)
        op = layout.operator_menu_enum(GmicOperator63.bl_idname, 'myprop', text=GmicOperator63.bl_label)
        op = layout.operator_menu_enum(GmicOperator64.bl_idname, 'myprop', text=GmicOperator64.bl_label)
        op = layout.operator_menu_enum(GmicOperator65.bl_idname, 'myprop', text=GmicOperator65.bl_label)


def register():
    bpy.utils.register_class(GmicOperator0)
    bpy.utils.register_class(GmicOperator1)
    bpy.utils.register_class(GmicOperator2)
    bpy.utils.register_class(GmicOperator3)
    bpy.utils.register_class(GmicOperator4)
    bpy.utils.register_class(GmicOperator5)
    bpy.utils.register_class(GmicOperator6)
    bpy.utils.register_class(GmicOperator7)
    bpy.utils.register_class(GmicOperator8)
    bpy.utils.register_class(GmicOperator9)
    bpy.utils.register_class(GmicOperator10)
    bpy.utils.register_class(GmicOperator11)
    bpy.utils.register_class(GmicOperator12)
    bpy.utils.register_class(GmicOperator13)
    bpy.utils.register_class(GmicOperator14)
    bpy.utils.register_class(GmicOperator15)
    bpy.utils.register_class(GmicOperator16)
    bpy.utils.register_class(GmicOperator17)
    bpy.utils.register_class(GmicOperator18)
    bpy.utils.register_class(GmicOperator19)
    bpy.utils.register_class(GmicOperator20)
    bpy.utils.register_class(GmicOperator21)
    bpy.utils.register_class(GmicOperator22)
    bpy.utils.register_class(GmicOperator23)
    bpy.utils.register_class(GmicOperator24)
    bpy.utils.register_class(GmicOperator25)
    bpy.utils.register_class(GmicOperator26)
    bpy.utils.register_class(GmicOperator27)
    bpy.utils.register_class(GmicOperator28)
    bpy.utils.register_class(GmicOperator29)
    bpy.utils.register_class(GmicOperator30)
    bpy.utils.register_class(GmicOperator31)
    bpy.utils.register_class(GmicOperator32)
    bpy.utils.register_class(GmicOperator33)
    bpy.utils.register_class(GmicOperator34)
    bpy.utils.register_class(GmicOperator35)
    bpy.utils.register_class(GmicOperator36)
    bpy.utils.register_class(GmicOperator37)
    bpy.utils.register_class(GmicOperator38)
    bpy.utils.register_class(GmicOperator39)
    bpy.utils.register_class(GmicOperator40)
    bpy.utils.register_class(GmicOperator41)
    bpy.utils.register_class(GmicOperator42)
    bpy.utils.register_class(GmicOperator43)
    bpy.utils.register_class(GmicOperator44)
    bpy.utils.register_class(GmicOperator45)
    bpy.utils.register_class(GmicOperator46)
    bpy.utils.register_class(GmicOperator47)
    bpy.utils.register_class(GmicOperator48)
    bpy.utils.register_class(GmicOperator49)
    bpy.utils.register_class(GmicOperator50)
    bpy.utils.register_class(GmicOperator51)
    bpy.utils.register_class(GmicOperator52)
    bpy.utils.register_class(GmicOperator53)
    bpy.utils.register_class(GmicOperator54)
    bpy.utils.register_class(GmicOperator55)
    bpy.utils.register_class(GmicOperator56)
    bpy.utils.register_class(GmicOperator57)
    bpy.utils.register_class(GmicOperator58)
    bpy.utils.register_class(GmicOperator59)
    bpy.utils.register_class(GmicOperator60)
    bpy.utils.register_class(GmicOperator61)
    bpy.utils.register_class(GmicOperator62)
    bpy.utils.register_class(GmicOperator63)
    bpy.utils.register_class(GmicOperator64)
    bpy.utils.register_class(GmicOperator65)
    bpy.utils.register_class(SimpleCustomMenu)

def unregister():
    bpy.utils.unregister_class(GmicOperator0)
    bpy.utils.unregister_class(GmicOperator1)
    bpy.utils.unregister_class(GmicOperator2)
    bpy.utils.unregister_class(GmicOperator3)
    bpy.utils.unregister_class(GmicOperator4)
    bpy.utils.unregister_class(GmicOperator5)
    bpy.utils.unregister_class(GmicOperator6)
    bpy.utils.unregister_class(GmicOperator7)
    bpy.utils.unregister_class(GmicOperator8)
    bpy.utils.unregister_class(GmicOperator9)
    bpy.utils.unregister_class(GmicOperator10)
    bpy.utils.unregister_class(GmicOperator11)
    bpy.utils.unregister_class(GmicOperator12)
    bpy.utils.unregister_class(GmicOperator13)
    bpy.utils.unregister_class(GmicOperator14)
    bpy.utils.unregister_class(GmicOperator15)
    bpy.utils.unregister_class(GmicOperator16)
    bpy.utils.unregister_class(GmicOperator17)
    bpy.utils.unregister_class(GmicOperator18)
    bpy.utils.unregister_class(GmicOperator19)
    bpy.utils.unregister_class(GmicOperator20)
    bpy.utils.unregister_class(GmicOperator21)
    bpy.utils.unregister_class(GmicOperator22)
    bpy.utils.unregister_class(GmicOperator23)
    bpy.utils.unregister_class(GmicOperator24)
    bpy.utils.unregister_class(GmicOperator25)
    bpy.utils.unregister_class(GmicOperator26)
    bpy.utils.unregister_class(GmicOperator27)
    bpy.utils.unregister_class(GmicOperator28)
    bpy.utils.unregister_class(GmicOperator29)
    bpy.utils.unregister_class(GmicOperator30)
    bpy.utils.unregister_class(GmicOperator31)
    bpy.utils.unregister_class(GmicOperator32)
    bpy.utils.unregister_class(GmicOperator33)
    bpy.utils.unregister_class(GmicOperator34)
    bpy.utils.unregister_class(GmicOperator35)
    bpy.utils.unregister_class(GmicOperator36)
    bpy.utils.unregister_class(GmicOperator37)
    bpy.utils.unregister_class(GmicOperator38)
    bpy.utils.unregister_class(GmicOperator39)
    bpy.utils.unregister_class(GmicOperator40)
    bpy.utils.unregister_class(GmicOperator41)
    bpy.utils.unregister_class(GmicOperator42)
    bpy.utils.unregister_class(GmicOperator43)
    bpy.utils.unregister_class(GmicOperator44)
    bpy.utils.unregister_class(GmicOperator45)
    bpy.utils.unregister_class(GmicOperator46)
    bpy.utils.unregister_class(GmicOperator47)
    bpy.utils.unregister_class(GmicOperator48)
    bpy.utils.unregister_class(GmicOperator49)
    bpy.utils.unregister_class(GmicOperator50)
    bpy.utils.unregister_class(GmicOperator51)
    bpy.utils.unregister_class(GmicOperator52)
    bpy.utils.unregister_class(GmicOperator53)
    bpy.utils.unregister_class(GmicOperator54)
    bpy.utils.unregister_class(GmicOperator55)
    bpy.utils.unregister_class(GmicOperator56)
    bpy.utils.unregister_class(GmicOperator57)
    bpy.utils.unregister_class(GmicOperator58)
    bpy.utils.unregister_class(GmicOperator59)
    bpy.utils.unregister_class(GmicOperator60)
    bpy.utils.unregister_class(GmicOperator61)
    bpy.utils.unregister_class(GmicOperator62)
    bpy.utils.unregister_class(GmicOperator63)
    bpy.utils.unregister_class(GmicOperator64)
    bpy.utils.unregister_class(GmicOperator65)
    bpy.utils.unregister_class(SimpleCustomMenu)

if __name__ == "__main__":
    register()

# The menu can also be called from scripts
bpy.ops.wm.call_menu(name=SimpleCustomMenu.bl_idname)

