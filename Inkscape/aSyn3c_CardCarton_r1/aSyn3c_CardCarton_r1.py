#!/usr/bin/env python3
# -*- coding: utf-8 -*-                                         #
##  Released under the GNU General Public License, version 3.  ##
##  For collaboration, write to cardcarton at asyn3c dot net.  ##
##_____________________________________________________________##
##  https://www.asyn3c.net/cardcarton/                         ##
##_____________________________________________________________##

from __future__ import division # python 3 provides true division by default #https://peps.python.org/pep-0238/ # was found in a scribus script
idstamping={'net.asyn3c.','inkscape.carton.','rev.0001.','ver.2023.04.10'}

## CONDENSE BUNDLED LIB NAME ##
import array as _a#############
import json as _j##############
import sys#####################
import os######################
###############################
import math as _b##############
import random as _y############
###############################
## SIMPLIFY BUNDLED LIB ONLY ##
import gettext as _g###########
_gt_ = _g.gettext##############
###############################
from lxml import etree as _x###
#from copy import deepcopy#####
###############################
from collections import ChainMap
## THIRD PARTY LIB PATH ################
sys.path.append('/usr/share/inkscape/extensions')
sys.path.append('/usr/share/scribus/scripts')
########################################
## THIRD PARTY LIB INCLUSION ###########

try:
  import inkex as _inx
  import simplepath as _inx_p
  import simplestyle as _inx_s
  #import pages as _pag
except ImportError as err:
  pass
  #print("No Inkscape")

try:
  import scribus
except ImportError as err:
  pass
  #print ("No Scribus")

########################################
## CLASSES FOLLOW FROM HERE ############



class aSyn3c91(_inx.Effect):
    def __init__(__):
        _inx.Effect.__init__(__)
        __._option_ = None # options as an object
        __._ = None # options as a hash
        __._root_ = None # document root
        __._page_ = None # document page
        __._register_ = None # grouplayer/outer
        __._geom_ = None # vector/inner
        __._stylesheet_ = None # style

        __.debug = None # simple console logging of coordinates
        __.session = None # sophisticated editing of blueprint/plans via spreadsheet

        # Requested item properties below.

        __.z0all0 = None
        __.z0job0 = None

        # It is up to the compliler, VM and the operating system to manage memory,
        # so let us stop splitting the related user preference and system plot data!
	# Each array below represents one tab & feature set of this macro; that is,
	# one tab & array for every step of the carton design and knifeline order.
	
        __.z1carton = None # one piece soft carton, user preferences
        __.z2rigbox = None # two piece hard boxshell, user preferences
        __.z3insert = None # stand-alone complex inserts
        __.z4impose = None # imposition plan
        __.z5outset = None # regular slotted container
        __.z6pallet = None # palletisation plan

        # In order to benefit from layers used for cut and crease,
        # as well as the ability to fade between current and previous dielines,
        # we really do need unique numbers to prefix or suffix these layer names,
        # or inkscape will assign unrecognisable numerical names for us.

        __.styleindex=0
        __.groupindex=0

        # These are old & deprecated, or recent & experimental arrays, intended
        # for reference and the testing and stable development of new features.

        #__.z0q0optional = None # User defined options
        #__.z0q1standard = None # Apply to all jobs (standard/expected)
        #__.z0q2specific = None # Apply to this job (specific/extender)
        
        #__.z3q1cutout = None # 
        #__.z3q2______ = None # 
        #__.z5q1handle = None # outer opposing grips
        #__.z5q2padder = None # inner padding for flatpack cartons



    def affect(__):
        __._root_ = __.document.getroot()
        __._page_ = __.svg.get_current_layer()

        ##https://wiki.inkscape.org/wiki/Generating_objects_from_extensions
        #parent = myself.svg.get_current_layer()
        ##https://www.linux-magazine.com/Issues/2020/239/Magic-Circle
        #option = myself.options

        # Every new document comes with a potentially unwanted 'layer1'.
        # Seriously, what are we going to do about that?
        # I can't remove it automatically because I will setup inkscape to crash if I try;
        # however, I can definitely remove layers I previously created.

        for element in __._root_.iter(tag=_x.Element):
          if element.eid[0:12]=='rootregister': # find the old registration mark
            element.getparent().remove(element) # bugger off! we will recreate these marks, every time.

        # The above, while predictably functional, removes the SVG root and crashes inkscape.
        # I need a cleaner method of purging this default layer.

            #if (
            #  element != __.document.getroot() and
            #  element.tag != _inx.addNS('g','svg') and
            #  element.tag != _inx.addNS('svg','svg') and
            #  element.tag != _inx.addNS('namedview','sodipodi') and
            #True ):
              #if __.debug[0] or __.debug[1]: _inx.utils.debug(['_layer1_',element.eid])
              #pass
    


    def effect(__):
        ## add_arguments() # automatically called by Inkscape prior to <class>.effect()
        __.get_arguments() # pre-processing of user supplied arguments
        __.affect() # Initialise workspace
        
        tab0=__._['tab'] # master notebook retains 'tab' name in spite of what I name it in the dialog definition

        #if tab0=='z0alltab':
        #  __.iffect_1({}) # will be deprecated in favor of __.ueffect_0( __._diagnose_ )
        #if tab0=='z0jobtab':
        #  __.iffect_2({}) # will be deprecated in favor of __.ueffect_0( __._register_ )

        #__.offect_0()
        #__.uffect_0([]) # diagnostic grid
        
        #__.uffect_1( [ __._fold_, __._chop_, __.z1carton['PlanWindow'][iz], __.z1carton['PlanInsert'][iz] ] )
        #__.uffect_1( ChainMap( __._fold_, __._chop_, __.z1carton['PlanWindow'][iz], __.z1carton['PlanInsert'][iz] ).items() )
        if tab0=='z1carton_tab' or tab0=='z0jobtab' or tab0=='z0alltab':
          __.offect_1()
          __.uffect_1( [] )
        if tab0=='z2rigbox_tab':
          __.offect_2()
          __.uffect_2( [] )
        if tab0=='z3insert_tab':
          __.offect_3()
          __.uffect_3( [] )
        if tab0=='z4impose_tab':
          __.offect_4()
          __.uffect_4( [] )
        if tab0=='z5outset_tab':
          __.offect_5()
          __.uffect_5( [] )
        if tab0=='z6pallet_tab':
          __.offect_6()
          __.uffect_6( [] )
        
        #__.uffect_0([]) # registration marks



    def iffect_1(__, requests):
        ##
        ## Registration Marks

        #_z01=_inx.elements._meta.Page.new(-40,40,-10,120)
        #_z02=__._page_.new(-40,160,-10,200)

        if __._['q_0all_plot_register']=='1':
          __.z0job0['page'][0]-=10 # required to keep all cut lines in the plotters working area.

          attribs = { 'style':str(_inx.Style(__._stylesheet_['q_register'])),
          _inx.addNS('label','inkscape') : "z1register01", 'd' :
          'M'+ str(10)+',' + str( 0)+
          'L'+ str( 0)+',' + str( 0)+
          'L'+ str( 0)+',' + str(10)+
          'M'+ str(10)+',' + str(10)+
          'L'+ str( 4)+',' + str( 4)+
          'M'+ str(__.z0job0['page'][0]-10)+',' + str(__.z0job0['page'][1]- 0)+
          'L'+ str(__.z0job0['page'][0]- 0)+',' + str(__.z0job0['page'][1]- 0)+
          'L'+ str(__.z0job0['page'][0]- 0)+',' + str(__.z0job0['page'][1]-10)+
          'M'+ str(__.z0job0['page'][0]-10)+',' + str(__.z0job0['page'][1]-10)+
          'L'+ str(__.z0job0['page'][0]- 4)+',' + str(__.z0job0['page'][1]- 4)+
          'M'+ str(10)+',' + str(__.z0job0['page'][1]- 0)+
          'L'+ str( 0)+',' + str(__.z0job0['page'][1]- 0)+
          'L'+ str( 0)+',' + str(__.z0job0['page'][1]-10)+
          'M'+ str(10)+',' + str(__.z0job0['page'][1]-10)+
          'L'+ str( 4)+',' + str(__.z0job0['page'][1]- 4)+
          'M'+ str(__.z0job0['page'][0]-10)+',' + str( 0)+
          'L'+ str(__.z0job0['page'][0]- 0)+',' + str( 0)+
          'L'+ str(__.z0job0['page'][0]- 0)+',' + str(10)+
          'M'+ str(__.z0job0['page'][0]-10)+',' + str(10)+
          'L'+ str(__.z0job0['page'][0]- 4)+',' + str( 4)+
          '' }
        
          __.z0job0['page'][0]+=10 # and we're back.

          diag = _x.SubElement(__._page_, _inx.addNS('path','svg'), attribs )
        
        elif __._['q_0all_plot_register']=='2' or __._['q_0all_plot_register']=='3':
         xxxx=float(__._root_.get('width')[:-2]) # trim 'mm'
         yyyy=float(__._root_.get('height')[:-2]) # trim 'mm'
         __._register_ = __._root_.add(_inx.Group()) # make a new group at entity level
         __._register_.set('id', 'rootregister') #__.svg.get_unique_id('iz--')
         __._register_.set(_inx.addNS('label', 'inkscape'),'Regmarks')
         _style=('q_register_kongsberg_1' if __._['q_0all_plot_register']=='3' else 'q_register_brother_1')
         for yy in range(2):
          for xx in range(2):
           ##https://www.linux-magazine.com/Issues/2020/239/Magic-Circle
           attribs = {
             'style': str(_inx.Style(__._stylesheet_[_style])),
             _inx.addNS('label', 'inkscape'): _style+
             '_{0:1X}_{1:1X}'.format(yy,xx),
             'cx': str(10+((xxxx*xx)-(20*xx))),
             'cy': str(10+((yyyy*yy)-(20*yy))),
             'r': '6.0'
           }
           __._register_.add(_inx.Circle (**attribs))
           if __.debug[0] or __.debug[1]: _inx.utils.debug([
             ['rego',__._['q_0all_plot_register'],],
             [yy,xx],[
               (xxxx*xx),
               (yyyy*yy),
             ],
           ])

          
        
    def iffect_2(__, requests):
      for iz in range(len(__.z1carton['Enable'])):
        ##
        ## Diagnostic Grid

        sD00=''
        for qZ in range(len(__.z1carton['GRID'][iz])-1): # Last element is the size minus offset.
          sD00+=\
          'M'+str(__.z1carton['GRID'][iz][qZ][0])+','+str(__.z1carton['GRID'][iz][0][1])+\
          'L'+str(__.z1carton['GRID'][iz][qZ][0])+','+str(__.z1carton['GRID'][iz][6][1])+\
          ''\
          'M'+str(__.z1carton['GRID'][iz][0][0])+','+str(__.z1carton['GRID'][iz][qZ][1])+\
          'L'+str(__.z1carton['GRID'][iz][6][0])+','+str(__.z1carton['GRID'][iz][qZ][1])+\
          ''

        attb = {'style':str(_inx.Style(__._stylesheet_['q_diagnose'])), _inx.addNS('label','inkscape') : "z1diagnose01", 'd' : sD00 }

        diag = _x.SubElement(__._page_, _inx.addNS('path','svg'), attb )



    def offect_0(__): # registration and diagnostic
        #_inx.utils.debug('[[0(00)0]]')
        pass

    def uffect_0(__, list00, item00):
      ##
      ## Plot anything:
      ##   Registration, Diagnostic,
      ##   Cartons, RigidBoxShells, Inserts, Outsets;
      ##   Imposition, and Palletisation plans.
      ## Palletisation plans are more of a report than artwork.
      ##   Associated drawings shall be imported into an openOffice document.
      #
      # Flags:
      # 0x0080, 128 - window geometry (viewable/accessable cutouts embedded into carton)
      # 0x0100, 256 - hanger geometry (point of sale extensions, for hook hanging)
      # 0x0200, 512 - insert geometry (internal padding for carton contents)
      # 0x0400, 1024- outset geometry (regular slotted container, sized for flat carton)
      # 0x0800, 2048- lid
      # 0x1000, 4096- base
      # 0x2000, 8192- swap sides (reverse-of-lid or same-side-as-lid for the base)
      #
      #{ **__._fold_, **__._chop_ }.items():
      #
      #_inx.utils.debug(ChainMap( __._fold_, __._chop_, __._window_, __._insert_ ).items())
      if isinstance(list00,list):
        style0='q_diagnose' # default to this stroke if the style is not properly defined!
        movecounting=0
        linecounting=0
        _last_move=[0.0,0.0]
        __._list_move=[]
        _this_move=[0.0,0.0]
        _text_plot=[0.0,0.0]

        ##https://inkscape.org/~MarioVoigt/%E2%98%85ungrouper-and-element-migratorfilter
        _layer = __.document.getroot().add(_inx.Group()) # make a new group at root level
        _layer.set(_inx.addNS('groupmode', 'inkscape'), 'layer') # Layers are at the top level only!
        _layer.set('id', 'item-'+str(item00)) #__.svg.get_unique_id('iz--')
        _layer.set(_inx.addNS('label', 'inkscape'),'Item '+str(item00))

        _regi_ = _layer.add(_inx.Group()) # make a new group at entity level
        _regi_.set('id', 'regi-'+str(item00)) #__.svg.get_unique_id('iz--')
        _regi_.set(_inx.addNS('label', 'inkscape'),'Regmarks')

        _diag_ = _layer.add(_inx.Group()) # make a new group at entity level
        _diag_.set('id', 'diag-'+str(item00)) #__.svg.get_unique_id('iz--')
        _diag_.set(_inx.addNS('label', 'inkscape'),'Plot')

        _fold_ = _layer.add(_inx.Group()) # make a new group at entity level
        _fold_.set('id', 'fold-'+str(item00)) #__.svg.get_unique_id('iz--')
        _fold_.set(_inx.addNS('label', 'inkscape'),'Crease')

        _chop_ = _layer.add(_inx.Group()) # make a new group at entity level
        _chop_.set('id', 'chop-'+str(item00)) #__.svg.get_unique_id('iz--')
        _chop_.set(_inx.addNS('label', 'inkscape'),'Full Cut')

        _doug_ = _diag_
        _rogi_ = _regi_
        
        for list01 in list00: #ChainMap( __._fold_, __._chop_, __._window_, __._insert_ ).items():
          flag_4=0 # flag for whole of brace; use a logical OR to join to each node flag.
          xml0=''
          if isinstance(list01,list):
            for list02 in list01:
              flag_3=0
              flag_2=0
              if isinstance(list02,list):
                for list03 in list02:
                  flag_1=0
                  b_plot=False
                  if not isinstance(list03,list):
                    if __.debug[0]: _inx.utils.debug('<3| '+list03.__str__()+' |3>')
                  elif (len(list03)==0): # Empty.
                    b_plot=False
                    if __.debug[0]: _inx.utils.debug('<3>')
                  elif (len(list03)==1): # One flag only; it will apply to all remaining elements of the brace.
                    if isinstance(list03[0],int):
                      flag_2=list03[0]
                      if __.debug[0]: _inx.utils.debug('<3# '+list03[0].__str__()+' #3>')
                    if isinstance(list03[0],str):
                      style0=list03[0]
                      if __.debug[0]: _inx.utils.debug('<3@ '+list03[0].__str__()+' @3>')
                  elif (len(list03)>=2): # One flag and one command; optional parameters.
                    if isinstance(list03[0],int): flag_1=list03[0]
                    flag_0=( flag_4 | flag_3 | flag_2 | flag_1 )
                    if __.debug[0]:
                      _inx.utils.debug('<3= '+','.join(map(str,list03))+' =3> |'+
                      str(flag_4)+'|'+str(flag_3)+'|'+str(flag_2)+'|-'+str(flag_1)+'-|='+str(flag_0)+'=|')
                    if (#b_plot=(
                      flag_0==0 or flag_0==1 or # yes to all fundamental segments!
                      ( ( (flag_0 & 0x08)==0x08 ) if __.z0job0['fullcube']=='half' else False) or
                      flag_0==128 or flag_0==512 or # yes to all window and insert segments!
                      flag_0==256 or flag_0==1024 or # yes to all hangsell and outset segments!
                      ( (flag_0 & 0x1800) & (0x0800) >0 and (
                        (flag_0 & 0x0066) & (0x0002 if __.z1carton['Lidd'][item00]=='c-lock' else 0x0000) >0 or # clip-lock
                        (flag_0 & 0x0066) & (0x0004 if __.z1carton['Lidd'][item00]=='p-lock' else 0x0000) >0 or # push-lock
                        (flag_0 & 0x0066) & (0x0006 if __.z1carton['Lidd'][item00]=='t-lock' else 0x0000) >0 or # tear-lock
                        False
                      ) and (flag_0 & 0x2000) == (0x0000 if __.z1carton['LiddOrient'][item00]=='F' else 0x2000) ) or
                      ( (flag_0 & 0x1800) & (0x1000) >0 and (
                        (flag_0 & 0x0066) & (0x0002 if __.z1carton['Base'][item00]=='c-lock' else 0x0000) >0 or # clip-lock
                        (flag_0 & 0x0066) & (0x0004 if __.z1carton['Base'][item00]=='p-lock' else 0x0000) >0 or # push-lock
                        (flag_0 & 0x0066) & (0x0006 if __.z1carton['Base'][item00]=='t-lock' else 0x0000) >0 or # tear-lock
                        (flag_0 & 0x0066) & (0x0020 if __.z1carton['Base'][item00]=='a-lock' else 0x0000) >0 or # auto-lock
                        (flag_0 & 0x0066) & (0x0040 if __.z1carton['Base'][item00]=='f-lock' else 0x0000) >0 or # full-lock
                        False
                      ) and (flag_0 & 0x2000) == (0x0000 if __.z1carton['BaseOrient'][item00]=='F' else 0x2000) ) or
                      False
                    ) and (
                      ( ( (flag_0 & 0x01)==0x00 ) if __.z0job0['fullcube']=='half' else True) and # no to full-cube only segments in a half cube
                      ( ( (flag_0 & 0x08)==0x00 ) if __.z0job0['fullcube']=='full' else True) and # no to half-cube only segments in a full cube
                      (flag_0 & 0x10)==0x00 and # no to disabled segments!
                      True
                      # no, that is, to tracing the plotting point journal of old ideas,
                      # which are included as a reference to improve future development.
                    ):#if b_plot==True:
                      if len(list03)==2: # Without paramaters, usually, this is a path terminator; an SVG 'z'.
                        xml0+=list03[1]+' '
                      elif len(list03)>=3: # With parameters, we accomodate the distribution of those below.
                        xml0+=' '.join(map(str,list03[1:]))
                        if list03[1]=='M':
                          movecounting+=1
                        elif list03[1]=='L' or list03[1]=='C':
                          linecounting+=1
                        ##https://www.w3schools.com/python/ref_string_format.asp
                        if list03[1]=='M' or list03[1]=='L' or list03[1]=='C':
                         circleoffset=(4 if list03[1]=='C' else 0)
                         circleradius=(1.00 if list03[1]=='M' else 0.25)
                         if __.debug[2]:
                          _this_move=[float(list03[2+circleoffset]),float(list03[3+circleoffset])]
                          _text_plot=_this_move
                          _found_count=0
                          for _that_move in __._list_move:
                            if(
                              (_this_move[0]>=_that_move[0]-4 and _this_move[0]<=_that_move[0]+25) and
                              (_this_move[1]>=_that_move[1]-3 and _this_move[1]<=_that_move[1]+((_found_count+3)*2))
                            ):
                              _found_count+=1
                              if (_this_move[1]>=_that_move[1]-2 and _this_move[1]<=_that_move[1]+4):
                                _found_count+=1
                              if __.debug[0] or __.debug[1]: _inx.utils.debug(['<>',_text_plot,'near',_that_move,'iter',_found_count])
                              #break # must go through complete list!
                          _text_plot[1]+=((_found_count)*2)
                          if _found_count==0:
                            if __.debug[0] or __.debug[1]: _inx.utils.debug(['==',_this_move,_last_move])
                          _stye_=__._stylesheet_['q_diagtype']
                          _stye_['fill']=__._stylesheet_[style0]['stroke'] # I want the font colour to match the current fold/chop stroke
                          _stye_['stroke']='#000000' # It is hard to see the lighter colours against a white page.
                          attribs = {
                            'style': str(_inx.Style(_stye_)),
                            _inx.addNS('label', 'inkscape'): '{0:04X}'.format(movecounting)+'--'+("T0" if list03[1]=='M' else "Tn--"+'{0:04X}'.format(linecounting)),
                            'x': '{0:+05.3f}'.format(_text_plot[0]),
                            'y': '{0:+05.3f}'.format(_text_plot[1]),
                          }
                          text = _inx.TextElement(**attribs)
                          text.set('xml:space', 'preserve')
                          text.text = 'X{0:+05.2f}, Y{1:+05.2f}; {2:04X}.'.format(float(list03[2+circleoffset]),float(list03[3+circleoffset]),movecounting)
                          _doug_.add(text)
                          _last_move=[float(list03[2+circleoffset]),float(list03[3+circleoffset])]
                          __._list_move.append(_last_move)
                         if __.debug[3]:
                          ## identify starting points
                          ##https://www.linux-magazine.com/Issues/2020/239/Magic-Circle
                          _stye_=__._stylesheet_['q_diagnose']
                          _stye_['stroke']=__._stylesheet_[style0]['stroke'] # I want the diagnostic stroke to match the current fold/chop stroke
                          attribs = {
                            'style': str(_inx.Style(_stye_)),
                            _inx.addNS('label', 'inkscape'): '{0:04X}'.format(movecounting)+'--'+("Move" if list03[1]=='M' else "Plot--"+'{0:04X}'.format(linecounting)),
                            'cx': str(list03[2+circleoffset]),
                            'cy': str(list03[3+circleoffset]),
                            'r': str(circleradius),
                          }
                          _doug_.add(_inx.Circle (**attribs))
                      if __.debug[1]: _inx.utils.debug('[3# '+list03.__str__()+' #3]')
              elif isinstance(list02,int):
                flag_3=list02
                if __.debug[0] or __.debug[1]: _inx.utils.debug('<2# '+list02.__str__()+' #2>')
              elif isinstance(list02,str):
                style0=list02
                _doug_ = _diag_.add(_inx.Group()) # make a new group at entity level
                _doug_.set('id', 'doug--'+'{0:04X}'.format(__.styleindex)) #__.svg.get_unique_id('iz--')
                __.styleindex+=0x10
                if __.debug[0] or __.debug[1]: _inx.utils.debug('<2@ '+list02.__str__()+' @2>')
          elif isinstance(list01,int):
            flag_4=list01
            if __.debug[0]: _inx.utils.debug('<1# '+list02.__str__()+' #1>')
          elif isinstance(list01,str):
            style0=list01
            if __.debug[0]: _inx.utils.debug('<1@ '+list02.__str__()+' @1>')

          if xml0!='': # plot only non-empty sets; presently, everything is being duplicated and some empty sets are triplicated.

            if __.debug[0] or __.debug[1]: _inx.utils.debug([style0[0:6],style0[6:]])
            
            attb={ \
              'style':str(_inx.Style(__._stylesheet_[style0])), \
              _inx.addNS('label','inkscape') : style0, 'd' : xml0 }
            if style0=='q_diagnose': _inx.utils.debug('[[  '+xml0+'  ]]')

            line=_x.SubElement(__._page_, \
            _inx.addNS('path','svg'), attb )
            ##https://alpha.inkscape.org/vectors/www.inkscapeforum.com/viewtopicf489.html?t=12849
            # alternate implementation syntax may be in above URL
            
            if style0[0:6]=='q_regi' or style0[0:6]=='q_rego':
              _regi_.insert(__.groupindex, line)
            elif style0[0:6]=='q_diag':
              _diag_.insert(__.groupindex, line)
            elif style0[0:6]=='q_fold':
              _fold_.insert(__.groupindex, line)
            elif style0[0:6]=='q_chop':
              _chop_.insert(__.groupindex, line)
            else:
              __._page_.insert(__.groupindex, line)

            __.groupindex += 0x10



    def offect_1(__): # 1 piece
      for iz in range(len(__.z1carton['Enable'])):
        ## [
        ##   0: number(classification), 1: letter(action),
        ##   2=X, 3=Y, 4-additional, 5-parameters,
        ## ]
        ## leading number for selective drawing: Bitwise flags determine inclusion.
        ## following letter for SVG path commands: [L]ine draw or [M]ove plot marker.
        ## trailing X and Y co-ordinates in millimetres.
        ## supplimentary co-ordinates for beizer curves.
        ## find the up-to-date table of segment selection in the final plot routine.

        ##https://docs.python.org/3/library/array.html
        ##https://www.w3schools.com/python/python_lists_add.asp

	##
        ## FF, constant
        __._geom_={
        # dust tab geometry
        'q_flap': {
          'inn':{
            'x':[0,2,4,0],
            'y':[0,2,6,0]}
          ,\
          'out':{
            'x':[0,0,4,8],
            'y':[0,2,6,0]}
        },
        # Crashlock flap geometry
        'q_crash_flap': {
          'x':[0,0],
          'y':[0,0],
        },
        # hangsell tab geometry
        'q_hang_tab': [\
          [8,8,10,12],\
          [0,0,2,3],],
        # hangsell pin geometry
        'q_hang_pin': [\
          [02.0,06.0,08.0,10.0,10.0,08.0,06.0,02.0,-02.0,-06.0,-08.0,-10.0,-10.0,-08.0,-06.0,-02.0],\
          [00.0,02.0,03.0,05.0,07.0,08.0,08.0,08.0, 08.0, 08.0, 08.0, 07.0, 05.0, 03.0, 02.0, 00.0],],
        }
    
        ##
        ## grid
        
        # For revision 2 and onward, I will convert this definition into the superior asymmetric grid.
        # In this revision 1, I want people to enjoy the simplicity of a symmetric grid for as long as practical.
        
        __.z1carton['GRID'][iz]={} # I wish for this to be a list; not a hash.
        # I cannot change it without breaking the iterative definition below.
        
        # zero is the point of origin in screen geometry; 0,0 is the upper left
        if iz==0: # First component offset:
          __.z1carton['GRID'][iz][0]= __.z0job0['offset'][0]
        else: # Next component offset:
          __.z1carton['GRID'][iz][0]= [
            __.z1carton['GRID'][iz-1][0][0],
            __.z1carton['GRID'][iz-1][7][1]+
            (__.z1carton['GRID'][iz-1][0][1]*3),
          ]
        # one and the one before last is the grid; X and Y axies are symmetrical.
        __.z1carton['GRID'][iz][1]= [ __.z1carton['GRID'][iz][0][0]+__._['q_tab_glue_diameter'], __.z1carton['GRID'][iz][0][1]+__._['q_tab_lid_diameter'] ] # Real Tab.
        __.z1carton['GRID'][iz][2]= [ __.z1carton['GRID'][iz][1][0]+__.z1carton['Leng'][iz], __.z1carton['GRID'][iz][1][1]+__.z1carton['Widt'][iz]+__._['q_crease_lid_hinge_outset'] ]
        __.z1carton['GRID'][iz][3]= [ __.z1carton['GRID'][iz][2][0]+__.z1carton['Widt'][iz], __.z1carton['GRID'][iz][2][1]+(__.z1carton['Heig'][iz]/2) ]
        __.z1carton['GRID'][iz][4]= [ __.z1carton['GRID'][iz][3][0]+__.z1carton['Leng'][iz], __.z1carton['GRID'][iz][2][1]+__.z1carton['Heig'][iz] ]
        __.z1carton['GRID'][iz][5]= [ __.z1carton['GRID'][iz][4][0]+__.z1carton['Widt'][iz]-__._['q_tab_glue_seam_reduction'], __.z1carton['GRID'][iz][4][1]+__.z1carton['Widt'][iz]+__._['q_crease_lid_hinge_outset'] ]
        __.z1carton['GRID'][iz][6]= [ __.z1carton['GRID'][iz][5][0]+__._['q_tab_glue_diameter'], __.z1carton['GRID'][iz][5][1]+__._['q_tab_lid_diameter'] ] # Phantom Tab!
        # last one is the total size as flat piece, without margin / point of origin
        __.z1carton['GRID'][iz][7]= [ __.z1carton['GRID'][iz][5][0]-__.z1carton['GRID'][iz][0][0], __.z1carton['GRID'][iz][6][1]-__.z1carton['GRID'][iz][0][1] ]
        # There is not a real right glue tab. Only the one on the left is present.
        # The calculation is included for the sake of reserving a safe margin of plotting area,
        # should the user have other ideas about what to do with the glue tab.
        #
        # The following paragraphs will both describe the tab reduction
        # settings, as well as illustrate the difference between the
        # major grid and minor grid used internally to brace blueprints.
        #
        # I have opted for ['q_tab_glue_seam_reduction'] to be part of
        # the major grid rather than the minor, as nearby tab components,
        # both array based, will be adjusted by this figure. Indeed;
        # the entire flat area is changed when this value is changed.
        #
        # An opposing counterpart, ['q_tab_glue_fold_reduction'], is part
        # of the minor grid because only one crease line has to be moved;
        # everything else can stay in its proper place.

        ##
        ## flap
        __.z1carton['FlapHeight'][iz]=(
          (__.z1carton['Leng'][iz]/2) if
          (__.z1carton['Leng'][iz]/2) < (__.z1carton['Widt'][iz]) else
          (__.z1carton['Widt'][iz]/1)
        )

        ##
        ## offset
        _liddoffset_=(0 if __.z1carton['LiddOrient'][iz]=='F' else 2)
        _baseoffset_=(0 if __.z1carton['BaseOrient'][iz]=='F' else 2)
       
        # window offset geometry
        __.z1carton['Window'][iz]['centre']={
        'x':[\
          __.z1carton['GRID'][iz][1+_liddoffset_][0]+(__.z1carton['Leng'][iz]/2),
          __.z1carton['GRID'][iz][1][0]+(__.z1carton['Leng'][iz]/2), __.z1carton['GRID'][iz][2][0]+(__.z1carton['Widt'][iz]/2),
          __.z1carton['GRID'][iz][3][0]+(__.z1carton['Leng'][iz]/2), __.z1carton['GRID'][iz][4][0]+(__.z1carton['Widt'][iz]/2), \
          __.z1carton['GRID'][iz][1+_baseoffset_][0]+(__.z1carton['Leng'][iz]/2)],
        'y':[\
          __.z1carton['GRID'][iz][1][1]+(__.z1carton['Widt'][iz]/2),
          __.z1carton['GRID'][iz][3][1], __.z1carton['GRID'][iz][3][1],
          __.z1carton['GRID'][iz][3][1], __.z1carton['GRID'][iz][3][1], \
          __.z1carton['GRID'][iz][4][1]+(__.z1carton['Widt'][iz]/2)]
        }
        # insert offset geometry
        __.z1carton['GridInsert'][iz]=[\
          [ __.z1carton['GRID'][iz][7][0]+(__.z0job0['offset'][0][0]*2)+(__.z0job0['offset'][1][0]*1),
            __.z1carton['GRID'][iz][0][1]+__.z0job0['offset'][1][1]-__.z0job0['offset'][0][1] ], \
          [ 0, __.z1carton['GRID'][iz][0][1]+__.z0job0['offset'][1][1]-__.z0job0['offset'][0][1] ], \
          [ 0, __.z1carton['GRID'][iz][0][1]+__.z0job0['offset'][1][1]-__.z0job0['offset'][0][1] ], \
          [ 0, __.z1carton['GRID'][iz][0][1]+__.z0job0['offset'][1][1]-__.z0job0['offset'][0][1] ], \
        ]
        for qZ in range(len(__.z1carton['GridInsert'][iz])):#(__.z1carton['GridInsert'][iz].buffer_info()[1]):
          ##
          ## relative adjustments for insert
          if __.z1carton['Insert'][iz]['Li'][qZ]<0:
            __.z1carton['Insert'][iz]['Li'][qZ]=__.z1carton['Leng'][iz]+__.z1carton['Insert'][iz]['Li'][qZ]
          if __.z1carton['Insert'][iz]['Wi'][qZ]<0:
            __.z1carton['Insert'][iz]['Wi'][qZ]=__.z1carton['Widt'][iz]+__.z1carton['Insert'][iz]['Wi'][qZ]
          if __.z1carton['Insert'][iz]['Hi'][qZ]<0:
            __.z1carton['Insert'][iz]['Hi'][qZ]=__.z1carton['Heig'][iz]+__.z1carton['Insert'][iz]['Hi'][qZ]
          if qZ>0:
            __.z1carton['GridInsert'][iz][qZ][0]=__.z1carton['GridInsert'][iz][qZ-1][0]+__.z1carton['Insert'][iz]['Li'][0]+__.z0job0['offset'][1][0]
            # it was necessary to go for initial offset rather than next component, tempoarily at least, because of how I use this for 2nd carton.

        ##
        ## hangsell extension
        _hangoffset_=(2 if __.z1carton['LiddOrient'][iz]=='F' else 0) # the hangtabb shall be positioned opposing the lid at all times.
        ##
        
        ##
        ## carton components
        _softcarton_={
        
         'common': {
         
          'glue-tab': {
          
           'L':[
            [ 0x0000 ], # This is the left side of the carton. ( Begin with a 'M'ove because current flap order introduces an unwanted line. )
            [ 0 , 'M', __.z1carton['GRID'][iz][1][0], __.z1carton['GRID'][iz][4][1], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][0][0], __.z1carton['GRID'][iz][4][1]-__._['q_tab_glue_taper'], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][0][0], __.z1carton['GRID'][iz][2][1]+__._['q_tab_glue_taper'], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][1][0], __.z1carton['GRID'][iz][2][1], ], # broken path, first point closure
            [ 16 , 'z', ], # 16=deprecated; close all our closed paths; half and full cube, any lid and base selection.
           ],
           'R':[
            [ 0x0001 ], # This is the right side of the carton. In one-piece production this phantom tab does not exist!
            [ 0 , 'M', __.z1carton['GRID'][iz][5][0], __.z1carton['GRID'][iz][2][1], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][6][0], __.z1carton['GRID'][iz][2][1]+__._['q_tab_glue_taper'], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][6][0], __.z1carton['GRID'][iz][4][1]-__._['q_tab_glue_taper'], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][5][0], __.z1carton['GRID'][iz][4][1], ], # broken path, first point closure
            [ 16 , 'z', ], # 16=deprecated; close all our closed paths; full cube only.
           ],
           
          },
          'hang-tab': {
          
           'outer': [ ## hangtabb (the hanging tab)
            [ (0x0903 if __.z1carton['LiddOrient'][iz]=='F' else 0x2903) ], # the remainder of this brace will be flagged as lid-geometry.
            [ 0 , 'L', __.z1carton['GRID'][iz][_hangoffset_+1][0]+__._geom_['q_hang_tab'][0][0], __.z1carton['GRID'][iz][2][1]-__._geom_['q_hang_tab'][1][0], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][_hangoffset_+1][0]+__._geom_['q_hang_tab'][0][1], __.z1carton['GRID'][iz][2][1]-__._geom_['q_hang_tab'][1][1]-__._['q_hang_tab_height'], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][_hangoffset_+1][0]+__._geom_['q_hang_tab'][0][2], __.z1carton['GRID'][iz][2][1]-__._geom_['q_hang_tab'][1][2]-__._['q_hang_tab_height'], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][_hangoffset_+1][0]+__._geom_['q_hang_tab'][0][3], __.z1carton['GRID'][iz][2][1]-__._geom_['q_hang_tab'][1][3]-__._['q_hang_tab_height'], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][_hangoffset_+2][0]-__._geom_['q_hang_tab'][0][3], __.z1carton['GRID'][iz][2][1]-__._geom_['q_hang_tab'][1][3]-__._['q_hang_tab_height'], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][_hangoffset_+2][0]-__._geom_['q_hang_tab'][0][2], __.z1carton['GRID'][iz][2][1]-__._geom_['q_hang_tab'][1][2]-__._['q_hang_tab_height'], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][_hangoffset_+2][0]-__._geom_['q_hang_tab'][0][1], __.z1carton['GRID'][iz][2][1]-__._geom_['q_hang_tab'][1][1]-__._['q_hang_tab_height'], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][_hangoffset_+2][0]-__._geom_['q_hang_tab'][0][0], __.z1carton['GRID'][iz][2][1]-__._geom_['q_hang_tab'][1][0], ],
           ],
           'inner': [ ## hangpinn (the hook hole)
           ], ## this component will be built with a functional loop, point by point.
           
          },
          'register': {
           'generic1': [
           ],
           'generic2': [
           ],
           'brother1': [
           ],
           'kongsberg1': [
           ],
          }, ## should we build these outside of this array initialisation? for now I say it depends on the consistency of shape.

         },
         
        } # Go straight from allocating one single static array, to adding multiple dynamic arrays.
        def _func_flap_base(flag, number, updown):
          if (flag& 0x02)!=0x02: # clip-lock lid and base design number
            return []

          offset=[0,0] # X is useful; Y not so much, until I can use a loop to reverse the order of the plotting below.
          offset[0]=0 if number==1 else 2 # closing walls &,    clockwise curves;

          #if updown==0:
          #  offset[0]=0 if number==1 else 2 # closing walls &,    clockwise curves;
          #if updown==1:
          #  offset[0]=2 if number==1 else 0 # ticking clocks...   efficient plots.
          _art=[
            [ flag ],
            [ 0 , 'M', __.z1carton['GRID'][iz][offset[0]+1][0], __.z1carton['GRID'][iz][offset[1]+2][1], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][offset[0]+1][0], __.z1carton['GRID'][iz][offset[1]+1][1], ],
            [ 0 , 'M', __.z1carton['GRID'][iz][offset[0]+1][0]+__._['q_tab_lid_reduce'], __.z1carton['GRID'][iz][offset[1]+1][1], ],
            [ 0 , 'C',
              (__.z1carton['GRID'][iz][offset[0]+1][0])+__._['q_tab_lid_reduce'], (__.z1carton['GRID'][iz][offset[1]+1][1])-(__._['q_tab_lid_diameter']*__._['q_tab_lid_curve_diameter']),
              (__.z1carton['GRID'][iz][offset[0]+1][0])+__._['q_tab_lid_reduce']+(__._['q_tab_lid_taper']*__._['q_tab_lid_curve_taper']), (__.z1carton['GRID'][iz][offset[1]+0][1]),
              (__.z1carton['GRID'][iz][offset[0]+1][0])+__._['q_tab_lid_reduce']+(__._['q_tab_lid_taper']), (__.z1carton['GRID'][iz][offset[1]+0][1]), ],
            [ 0 , 'L', __.z1carton['GRID'][iz][offset[0]+2][0]-__._['q_tab_lid_reduce']-__._['q_tab_lid_taper'], __.z1carton['GRID'][iz][offset[1]+0][1], ],
            [ 0 , 'C',
              (__.z1carton['GRID'][iz][offset[0]+2][0])-__._['q_tab_lid_reduce']-(__._['q_tab_lid_taper']*__._['q_tab_lid_curve_taper']), (__.z1carton['GRID'][iz][offset[1]+0][1]),
              (__.z1carton['GRID'][iz][offset[0]+2][0])-__._['q_tab_lid_reduce'], (__.z1carton['GRID'][iz][offset[1]+1][1])-(__._['q_tab_lid_diameter']*__._['q_tab_lid_curve_diameter']),
              (__.z1carton['GRID'][iz][offset[0]+2][0])-__._['q_tab_lid_reduce'], (__.z1carton['GRID'][iz][offset[1]+1][1]), ],
            [ 0 , 'M', __.z1carton['GRID'][iz][offset[0]+2][0], __.z1carton['GRID'][iz][offset[1]+1][1], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][offset[0]+2][0], __.z1carton['GRID'][iz][offset[1]+2][1], ],
          ] if (flag& 0x1000)==0x0000 else [
            [ flag ],
            [ 0 , 'M', __.z1carton['GRID'][iz][offset[0]+2][0], __.z1carton['GRID'][iz][offset[1]+4][1], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][offset[0]+2][0], __.z1carton['GRID'][iz][offset[1]+5][1], ],
            [ 0 , 'M', __.z1carton['GRID'][iz][offset[0]+2][0]-__._['q_tab_lid_reduce'], __.z1carton['GRID'][iz][offset[1]+5][1], ],
            [ 0 , 'C',
              (__.z1carton['GRID'][iz][offset[0]+2][0])-__._['q_tab_lid_reduce'], (__.z1carton['GRID'][iz][offset[1]+5][1])+(__._['q_tab_lid_diameter']*__._['q_tab_lid_curve_diameter']),
              (__.z1carton['GRID'][iz][offset[0]+2][0])-__._['q_tab_lid_reduce']-(__._['q_tab_lid_taper']*__._['q_tab_lid_curve_taper']), (__.z1carton['GRID'][iz][offset[1]+5][1])+(__._['q_tab_lid_diameter']),
              (__.z1carton['GRID'][iz][offset[0]+2][0])-__._['q_tab_lid_reduce']-(__._['q_tab_lid_taper']), (__.z1carton['GRID'][iz][offset[1]+5][1])+(__._['q_tab_lid_diameter']), ],
            [ 0 , 'L', __.z1carton['GRID'][iz][offset[0]+1][0]+__._['q_tab_lid_reduce']+__._['q_tab_lid_taper'], __.z1carton['GRID'][iz][offset[1]+5][1]+__._['q_tab_lid_diameter'], ],
            [ 0 , 'C',
              (__.z1carton['GRID'][iz][offset[0]+1][0])+__._['q_tab_lid_reduce']+(__._['q_tab_lid_taper']*__._['q_tab_lid_curve_taper']), (__.z1carton['GRID'][iz][offset[1]+5][1])+(__._['q_tab_lid_diameter']),
              (__.z1carton['GRID'][iz][offset[0]+1][0])+__._['q_tab_lid_reduce'], (__.z1carton['GRID'][iz][offset[1]+5][1])+(__._['q_tab_lid_diameter']*__._['q_tab_lid_curve_diameter']),
              (__.z1carton['GRID'][iz][offset[0]+1][0])+__._['q_tab_lid_reduce'], (__.z1carton['GRID'][iz][offset[1]+5][1]), ],
            [ 0 , 'M', __.z1carton['GRID'][iz][offset[0]+1][0], __.z1carton['GRID'][iz][offset[1]+5][1], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][offset[0]+1][0], __.z1carton['GRID'][iz][offset[1]+4][1], ],
          ]
          return(_art)
        def _func_flap_dust(flag):
          if (flag& 0x02)!=0x02: # clip-lock lid and base design number
            return []
          _art=[
            [ flag ],
          ]
          return(_art)
          
        _softcarton_['cliplock']={
         
          'outer-edge': {
          
           'A1':
            _softcarton_['common']['hang-tab']['outer'] if
            __.z1carton['Hang'][iz]=='1' and __.z1carton['LiddOrient'][iz]=='F'
              else [
            [ 0x0803 ],
            [ 0 , 'M', __.z1carton['GRID'][iz][3][0], __.z1carton['GRID'][iz][2][1], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][4][0], __.z1carton['GRID'][iz][2][1], ],
           ],
           'A2':
            _softcarton_['common']['hang-tab']['outer'] if
            __.z1carton['Hang'][iz]=='1' and __.z1carton['LiddOrient'][iz]=='R'
              else [
            [ 0x2802 ],
            [ 0 , 'M', __.z1carton['GRID'][iz][1][0], __.z1carton['GRID'][iz][2][1], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][2][0], __.z1carton['GRID'][iz][2][1], ],
           ],
           'B1': [
            [ 0x1002 ],
            [ 0 , 'M', __.z1carton['GRID'][iz][4][0], __.z1carton['GRID'][iz][4][1], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][3][0], __.z1carton['GRID'][iz][4][1], ],
           ],
           'B2': [
            [ 0x3003 ],
            [ 0 , 'M', __.z1carton['GRID'][iz][2][0], __.z1carton['GRID'][iz][4][1], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][1][0], __.z1carton['GRID'][iz][4][1], ],
           ],

          },
          'outer-flap': {

           'A1': _func_flap_base( 0x0802, 1, 0 ), # this brace will be flagged as forward-side lid-geometry.
           'A2': _func_flap_base( 0x2803, 2, 0 ), # this brace will be flagged as reverse-side lid-geometry.
           'B1': _func_flap_base( 0x1003, 1, 1 ), # this brace will be flagged as forward-side bum-geometry.
           'B2': _func_flap_base( 0x3002, 2, 1 ), # this brace will be flagged as reverse-side bum-geometry.

          },
          'inner-flap': {

           'A1i1': [
            [ 0x0802 ],
            [ 0 , 'M', __.z1carton['GRID'][iz][2][0]+__._geom_['q_flap']['inn']['x'][0], __.z1carton['GRID'][iz][2][1]-__._geom_['q_flap']['inn']['y'][0], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][2][0]+__._['q_tab_dust_seam_reduction']+__._geom_['q_flap']['inn']['x'][1], __.z1carton['GRID'][iz][2][1]-__._geom_['q_flap']['inn']['y'][1], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][2][0]+__._['q_tab_dust_seam_reduction']+__._geom_['q_flap']['inn']['x'][2], __.z1carton['GRID'][iz][2][1]-__._geom_['q_flap']['inn']['y'][2], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][2][0]+__._['q_tab_dust_seam_reduction']+__._geom_['q_flap']['inn']['x'][2], __.z1carton['GRID'][iz][2][1]+__._geom_['q_flap']['inn']['y'][3]-__.z1carton['FlapHeight'][iz], ],
          ] if __.z1carton['Flap'][iz]==1 else [
            [ 0x0802 ],
            [ 0 , 'M', __.z1carton['GRID'][iz][2][0], __.z1carton['GRID'][iz][2][1]-__.z1carton['FlapHeight'][iz], ],
            # bug: The 'Move' commencing this flap once drew a line from the previous 'Move' commencing the lid; I do not know why.
            ],
           'A1o1': [
            [ 0x0802 ],
            [ 0 , 'L', __.z1carton['GRID'][iz][3][0]-__._['q_tab_dust_seam_reduction']-__._geom_['q_flap']['out']['x'][3], __.z1carton['GRID'][iz][2][1]+__._geom_['q_flap']['out']['y'][3]-__.z1carton['FlapHeight'][iz], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][3][0]-__._['q_tab_dust_seam_reduction']-__._geom_['q_flap']['out']['x'][2], __.z1carton['GRID'][iz][2][1]-__._geom_['q_flap']['out']['y'][2], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][3][0]-__._['q_tab_dust_seam_reduction']-__._geom_['q_flap']['out']['x'][1], __.z1carton['GRID'][iz][2][1]-__._geom_['q_flap']['out']['y'][1], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][3][0]-__._['q_tab_dust_seam_reduction']-__._geom_['q_flap']['out']['x'][0], __.z1carton['GRID'][iz][2][1]-__._geom_['q_flap']['out']['y'][0], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][3][0], __.z1carton['GRID'][iz][2][1], ],
            ],

           'A1i2': [
            [ 0x0803 ],
            [ 0 , 'M', __.z1carton['GRID'][iz][4][0], __.z1carton['GRID'][iz][2][1], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][4][0]+__._['q_tab_dust_seam_reduction']+__._geom_['q_flap']['out']['x'][0], __.z1carton['GRID'][iz][2][1]-__._geom_['q_flap']['out']['y'][0], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][4][0]+__._['q_tab_dust_seam_reduction']+__._geom_['q_flap']['out']['x'][1], __.z1carton['GRID'][iz][2][1]-__._geom_['q_flap']['out']['y'][1], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][4][0]+__._['q_tab_dust_seam_reduction']+__._geom_['q_flap']['out']['x'][2], __.z1carton['GRID'][iz][2][1]-__._geom_['q_flap']['out']['y'][2], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][4][0]+__._['q_tab_dust_seam_reduction']+__._geom_['q_flap']['out']['x'][3], __.z1carton['GRID'][iz][2][1]+__._geom_['q_flap']['out']['y'][3]-__.z1carton['FlapHeight'][iz], ],
            ],
           'A1o2': [
            [ 0x0803 ],
            [ 0 , 'L', __.z1carton['GRID'][iz][5][0]-__._geom_['q_flap']['inn']['x'][2], __.z1carton['GRID'][iz][2][1]+__._geom_['q_flap']['inn']['y'][3]-__.z1carton['FlapHeight'][iz], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][5][0]-__._geom_['q_flap']['inn']['x'][2], __.z1carton['GRID'][iz][2][1]-__._geom_['q_flap']['inn']['y'][2], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][5][0]-__._geom_['q_flap']['inn']['x'][1], __.z1carton['GRID'][iz][2][1]-__._geom_['q_flap']['inn']['y'][1], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][5][0]-__._geom_['q_flap']['inn']['x'][0], __.z1carton['GRID'][iz][2][1]-__._geom_['q_flap']['inn']['y'][0], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][5][0], __.z1carton['GRID'][iz][2][1], ],
          ] if __.z1carton['Flap'][iz]==1 else [
            [ 0x0803 ],
            [ 0 , 'L', __.z1carton['GRID'][iz][5][0], __.z1carton['GRID'][iz][2][1]-__.z1carton['FlapHeight'][iz], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][5][0], __.z1carton['GRID'][iz][2][1], ],
            ],

           'A2i1': [
            [ 0x2802 ],
            [ 0 , 'M', __.z1carton['GRID'][iz][2][0]+__._['q_tab_dust_seam_reduction']+__._geom_['q_flap']['out']['x'][0], __.z1carton['GRID'][iz][2][1]-__._geom_['q_flap']['inn']['y'][0], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][2][0]+__._['q_tab_dust_seam_reduction']+__._geom_['q_flap']['out']['x'][1], __.z1carton['GRID'][iz][2][1]-__._geom_['q_flap']['inn']['y'][1], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][2][0]+__._['q_tab_dust_seam_reduction']+__._geom_['q_flap']['out']['x'][2], __.z1carton['GRID'][iz][2][1]-__._geom_['q_flap']['inn']['y'][2], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][2][0]+__._['q_tab_dust_seam_reduction']+__._geom_['q_flap']['out']['x'][3], __.z1carton['GRID'][iz][2][1]+__._geom_['q_flap']['inn']['y'][3]-__.z1carton['FlapHeight'][iz], ],
            ],
           'A2o1': [
            [ 0x2802 ],
            [ 0 , 'L', __.z1carton['GRID'][iz][3][0]-__._geom_['q_flap']['inn']['x'][2], __.z1carton['GRID'][iz][2][1]+__._geom_['q_flap']['out']['y'][3]-__.z1carton['FlapHeight'][iz], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][3][0]-__._geom_['q_flap']['inn']['x'][2], __.z1carton['GRID'][iz][2][1]-__._geom_['q_flap']['out']['y'][2], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][3][0]-__._geom_['q_flap']['inn']['x'][1], __.z1carton['GRID'][iz][2][1]-__._geom_['q_flap']['out']['y'][1], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][3][0]-__._geom_['q_flap']['inn']['x'][0], __.z1carton['GRID'][iz][2][1]-__._geom_['q_flap']['out']['y'][0], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][3][0], __.z1carton['GRID'][iz][2][1], ],
          ] if __.z1carton['Flap'][iz]==1 else [
            [ 0x2802 ],
            #[ 0 , 'L', __.z1carton['GRID'][iz][2][0], __.z1carton['GRID'][iz][2][1], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][3][0], __.z1carton['GRID'][iz][2][1]-__.z1carton['FlapHeight'][iz], ],
            #[ 0 , 'L', __.z1carton['GRID'][iz][3][0], __.z1carton['GRID'][iz][2][1], ],
            # bug: The 'Move' commencing this flap once drew a line from the previous 'Move' commencing the lid; I do not know why.
            ],

           'A2i2': [
            [ 0x2803 ],
            [ 0 , 'M', __.z1carton['GRID'][iz][4][0], __.z1carton['GRID'][iz][2][1], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][4][0]+__._geom_['q_flap']['inn']['x'][0], __.z1carton['GRID'][iz][2][1]-__._geom_['q_flap']['out']['y'][0], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][4][0]+__._geom_['q_flap']['inn']['x'][1], __.z1carton['GRID'][iz][2][1]-__._geom_['q_flap']['out']['y'][1], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][4][0]+__._geom_['q_flap']['inn']['x'][2], __.z1carton['GRID'][iz][2][1]-__._geom_['q_flap']['out']['y'][2], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][4][0]+__._geom_['q_flap']['inn']['x'][2], __.z1carton['GRID'][iz][2][1]+__._geom_['q_flap']['out']['y'][3]-__.z1carton['FlapHeight'][iz], ],
          ] if __.z1carton['Flap'][iz]==1 else [
            [ 0x2803 ],
            [ 0 , 'M', __.z1carton['GRID'][iz][4][0], __.z1carton['GRID'][iz][2][1]-__.z1carton['FlapHeight'][iz], ],
            ],
           'A2o2': [
            [ 0x2803 ],
            [ 0 , 'L', __.z1carton['GRID'][iz][5][0]-__._geom_['q_flap']['out']['x'][3], __.z1carton['GRID'][iz][2][1]+__._geom_['q_flap']['inn']['y'][3]-__.z1carton['FlapHeight'][iz], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][5][0]-__._geom_['q_flap']['out']['x'][2], __.z1carton['GRID'][iz][2][1]-__._geom_['q_flap']['inn']['y'][2], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][5][0]-__._geom_['q_flap']['out']['x'][1], __.z1carton['GRID'][iz][2][1]-__._geom_['q_flap']['inn']['y'][1], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][5][0]-__._geom_['q_flap']['out']['x'][0], __.z1carton['GRID'][iz][2][1]-__._geom_['q_flap']['inn']['y'][0], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][5][0], __.z1carton['GRID'][iz][2][1], ],
            ],

           'B1i1': [
            [ 0x1003 ], ##------------## Lower Forward-Side Clip-Lock
            [ 0 , 'M', __.z1carton['GRID'][iz][5][0]-__._geom_['q_flap']['inn']['x'][0], __.z1carton['GRID'][iz][4][1]+__._geom_['q_flap']['inn']['y'][0], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][5][0]-__._geom_['q_flap']['inn']['x'][1], __.z1carton['GRID'][iz][4][1]+__._geom_['q_flap']['inn']['y'][1], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][5][0]-__._geom_['q_flap']['inn']['x'][2], __.z1carton['GRID'][iz][4][1]+__._geom_['q_flap']['inn']['y'][2], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][5][0]-__._geom_['q_flap']['inn']['x'][2], __.z1carton['GRID'][iz][4][1]+__.z1carton['FlapHeight'][iz]-__._geom_['q_flap']['inn']['y'][3], ],
          ] if __.z1carton['Flap'][iz]==1 else [
            [ 0x1003 ],
            [ 0 , 'M', __.z1carton['GRID'][iz][5][0], __.z1carton['GRID'][iz][4][1], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][5][0], __.z1carton['GRID'][iz][4][1]+__.z1carton['FlapHeight'][iz], ],
            #[ 0 , 'L', __.z1carton['GRID'][iz][4][0], __.z1carton['GRID'][iz][4][1], ],
            ],
           'B1o1': [
            [ 0x1003 ],
            [ 0 , 'L', __.z1carton['GRID'][iz][4][0]+__._['q_tab_dust_seam_reduction']+__._geom_['q_flap']['out']['x'][3], __.z1carton['GRID'][iz][4][1]+__.z1carton['FlapHeight'][iz]-__._geom_['q_flap']['out']['y'][3], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][4][0]+__._['q_tab_dust_seam_reduction']+__._geom_['q_flap']['out']['x'][2], __.z1carton['GRID'][iz][4][1]+__._geom_['q_flap']['out']['y'][2], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][4][0]+__._['q_tab_dust_seam_reduction']+__._geom_['q_flap']['out']['x'][1], __.z1carton['GRID'][iz][4][1]+__._geom_['q_flap']['out']['y'][1], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][4][0]+__._['q_tab_dust_seam_reduction']+__._geom_['q_flap']['out']['x'][0], __.z1carton['GRID'][iz][4][1]+__._geom_['q_flap']['out']['y'][0], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][4][0], __.z1carton['GRID'][iz][4][1], ],
            ],

           'B1i2': [
            [ 0x1002 ],
            [ 0 , 'M', __.z1carton['GRID'][iz][3][0]-__._['q_tab_dust_seam_reduction']-__._geom_['q_flap']['out']['x'][0], __.z1carton['GRID'][iz][4][1]+__._geom_['q_flap']['out']['y'][0], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][3][0]-__._['q_tab_dust_seam_reduction']-__._geom_['q_flap']['out']['x'][1], __.z1carton['GRID'][iz][4][1]+__._geom_['q_flap']['out']['y'][1], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][3][0]-__._['q_tab_dust_seam_reduction']-__._geom_['q_flap']['out']['x'][2], __.z1carton['GRID'][iz][4][1]+__._geom_['q_flap']['out']['y'][2], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][3][0]-__._['q_tab_dust_seam_reduction']-__._geom_['q_flap']['out']['x'][3], __.z1carton['GRID'][iz][4][1]+__.z1carton['FlapHeight'][iz]-__._geom_['q_flap']['out']['y'][3], ],
            ],
           'B1o2': [
            [ 0x1002 ],
            [ 0 , 'L', __.z1carton['GRID'][iz][2][0]+__._['q_tab_dust_seam_reduction']+__._geom_['q_flap']['inn']['x'][2], __.z1carton['GRID'][iz][4][1]+__.z1carton['FlapHeight'][iz]-__._geom_['q_flap']['inn']['y'][3], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][2][0]+__._['q_tab_dust_seam_reduction']+__._geom_['q_flap']['inn']['x'][2], __.z1carton['GRID'][iz][4][1]+__._geom_['q_flap']['inn']['y'][2], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][2][0]+__._['q_tab_dust_seam_reduction']+__._geom_['q_flap']['inn']['x'][1], __.z1carton['GRID'][iz][4][1]+__._geom_['q_flap']['inn']['y'][1], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][2][0]+__._geom_['q_flap']['inn']['x'][0], __.z1carton['GRID'][iz][4][1]+__._geom_['q_flap']['inn']['y'][0], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][2][0], __.z1carton['GRID'][iz][4][1], ],
          ] if __.z1carton['Flap'][iz]==1 else [
            [ 0x1002 ],
            [ 0 , 'L', __.z1carton['GRID'][iz][2][0], __.z1carton['GRID'][iz][4][1]+__.z1carton['FlapHeight'][iz], ],
            #[ 0 , 'L', __.z1carton['GRID'][iz][2][0], __.z1carton['GRID'][iz][4][1], ],
            ],

           'B2i1': [
            [ 0x3003 ], ##------------## Lower Reverse-Side Clip-Lock
            [ 0 , 'M', __.z1carton['GRID'][iz][5][0]-__._geom_['q_flap']['out']['x'][0], __.z1carton['GRID'][iz][4][1]+__._geom_['q_flap']['inn']['y'][0], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][5][0]-__._geom_['q_flap']['out']['x'][1], __.z1carton['GRID'][iz][4][1]+__._geom_['q_flap']['inn']['y'][1], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][5][0]-__._geom_['q_flap']['out']['x'][2], __.z1carton['GRID'][iz][4][1]+__._geom_['q_flap']['inn']['y'][2], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][5][0]-__._geom_['q_flap']['out']['x'][3], __.z1carton['GRID'][iz][4][1]+__.z1carton['FlapHeight'][iz]-__._geom_['q_flap']['inn']['y'][3], ],
            ],
           'B2o1': [
            [ 0x3003 ],
            [ 0 , 'L', __.z1carton['GRID'][iz][4][0]+__._geom_['q_flap']['inn']['x'][2], __.z1carton['GRID'][iz][4][1]+__.z1carton['FlapHeight'][iz]-__._geom_['q_flap']['out']['y'][3], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][4][0]+__._geom_['q_flap']['inn']['x'][2], __.z1carton['GRID'][iz][4][1]+__._geom_['q_flap']['out']['y'][2], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][4][0]+__._geom_['q_flap']['inn']['x'][1], __.z1carton['GRID'][iz][4][1]+__._geom_['q_flap']['out']['y'][1], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][4][0]+__._geom_['q_flap']['inn']['x'][0], __.z1carton['GRID'][iz][4][1]+__._geom_['q_flap']['out']['y'][0], ],
            #[ 0 , 'L', __.z1carton['GRID'][iz][4][0], __.z1carton['GRID'][iz][4][1], ],
          ] if __.z1carton['Flap'][iz]==1 else [
            [ 0x3003 ],
            [ 0 , 'L', __.z1carton['GRID'][iz][4][0], __.z1carton['GRID'][iz][4][1]+__.z1carton['FlapHeight'][iz], ],
            #[ 0 , 'L', __.z1carton['GRID'][iz][4][0], __.z1carton['GRID'][iz][4][1], ],
           ],

           'B2i2': [
            [ 0x3002 ],
            [ 0 , 'M', __.z1carton['GRID'][iz][3][0]-__._geom_['q_flap']['inn']['x'][0], __.z1carton['GRID'][iz][4][1]+__._geom_['q_flap']['out']['y'][0], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][3][0]-__._geom_['q_flap']['inn']['x'][1], __.z1carton['GRID'][iz][4][1]+__._geom_['q_flap']['out']['y'][1], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][3][0]-__._geom_['q_flap']['inn']['x'][2], __.z1carton['GRID'][iz][4][1]+__._geom_['q_flap']['out']['y'][2], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][3][0]-__._geom_['q_flap']['inn']['x'][2], __.z1carton['GRID'][iz][4][1]+__.z1carton['FlapHeight'][iz]-__._geom_['q_flap']['out']['y'][3], ],
          ] if __.z1carton['Flap'][iz]==1 else [
            [ 0x3002 ],
            [ 0 , 'M', __.z1carton['GRID'][iz][3][0], __.z1carton['GRID'][iz][4][1]+__.z1carton['FlapHeight'][iz], ],
           ],
           'B2o2': [
            [ 0x3002 ],
            [ 0 , 'L', __.z1carton['GRID'][iz][2][0]+__._['q_tab_dust_seam_reduction']+__._geom_['q_flap']['out']['x'][3], __.z1carton['GRID'][iz][4][1]+__.z1carton['FlapHeight'][iz]-__._geom_['q_flap']['inn']['y'][3], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][2][0]+__._['q_tab_dust_seam_reduction']+__._geom_['q_flap']['out']['x'][2], __.z1carton['GRID'][iz][4][1]+__._geom_['q_flap']['inn']['y'][2], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][2][0]+__._['q_tab_dust_seam_reduction']+__._geom_['q_flap']['out']['x'][1], __.z1carton['GRID'][iz][4][1]+__._geom_['q_flap']['inn']['y'][1], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][2][0]+__._['q_tab_dust_seam_reduction']+__._geom_['q_flap']['out']['x'][0], __.z1carton['GRID'][iz][4][1]+__._geom_['q_flap']['inn']['y'][0], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][2][0], __.z1carton['GRID'][iz][4][1], ],
           ],

          },

        }
        _softcarton_['tearlock']={

          '0':{
           '0':[
           ]
          }

        }
        _softcarton_['pushlock']={

          'onepiece':{

           'forward':[

            [ 0x1005 ], ##------------## Lower Forward-Side Push-Lock
            [ 0 , 'L', __.z1carton['GRID'][iz][5][0]-0, __.z1carton['GRID'][iz][4][1]+(__.z1carton['Leng'][iz]/2), ],
            [ 0 , 'L', __.z1carton['GRID'][iz][5][0]-(__.z1carton['Widt'][iz]*0.20), __.z1carton['GRID'][iz][4][1]+(__.z1carton['Leng'][iz]/2), ],
            [ 0 , 'L', __.z1carton['GRID'][iz][5][0]-(__.z1carton['Widt'][iz]*0.20), __.z1carton['GRID'][iz][4][1]+(__.z1carton['Leng'][iz]/2)-__._['q_tab_glue_diameter'], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][4][0]+3, __.z1carton['GRID'][iz][4][1]+3, ],

            [ 0 , 'L', __.z1carton['GRID'][iz][4][0], __.z1carton['GRID'][iz][4][1], ],

            [ 0 , 'L', __.z1carton['GRID'][iz][4][0]-(__.z1carton['Leng'][iz]*0.10), __.z1carton['GRID'][iz][4][1]+(__.z1carton['Widt'][iz]*0.75), ],
            [ 0 , 'L', __.z1carton['GRID'][iz][4][0]-(__.z1carton['Leng'][iz]*0.20), __.z1carton['GRID'][iz][4][1]+(__.z1carton['Widt'][iz]*0.75), ],
            [ 0 , 'L', __.z1carton['GRID'][iz][4][0]-(__.z1carton['Leng'][iz]*0.20), __.z1carton['GRID'][iz][4][1]+(__.z1carton['Widt'][iz]*0.45), ],
            [ 0 , 'L', __.z1carton['GRID'][iz][3][0]+(__.z1carton['Leng'][iz]*0.20), __.z1carton['GRID'][iz][4][1]+(__.z1carton['Widt'][iz]*0.45), ],
            [ 0 , 'L', __.z1carton['GRID'][iz][3][0]+(__.z1carton['Leng'][iz]*0.20), __.z1carton['GRID'][iz][4][1]+(__.z1carton['Widt'][iz]*0.75), ],
            [ 0 , 'L', __.z1carton['GRID'][iz][3][0]+(__.z1carton['Leng'][iz]*0.10), __.z1carton['GRID'][iz][4][1]+(__.z1carton['Widt'][iz]*0.75), ],

            [ 0 , 'L', __.z1carton['GRID'][iz][3][0], __.z1carton['GRID'][iz][4][1], ],

            [ 0 , 'L', __.z1carton['GRID'][iz][3][0]-3, __.z1carton['GRID'][iz][4][1]+3, ],
            [ 0 , 'L', __.z1carton['GRID'][iz][2][0]+(__.z1carton['Widt'][iz]*0.20), __.z1carton['GRID'][iz][4][1]+(__.z1carton['Leng'][iz]/2)-__._['q_tab_glue_diameter'], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][2][0]+(__.z1carton['Widt'][iz]*0.20), __.z1carton['GRID'][iz][4][1]+(__.z1carton['Leng'][iz]/2), ],
            [ 0 , 'L', __.z1carton['GRID'][iz][2][0]+0, __.z1carton['GRID'][iz][4][1]+(__.z1carton['Leng'][iz]/2), ],

            [ 0 , 'L', __.z1carton['GRID'][iz][2][0], __.z1carton['GRID'][iz][4][1], ],

            [ 0 , 'L', __.z1carton['GRID'][iz][2][0]-(__.z1carton['Leng'][iz]*0.21), __.z1carton['GRID'][iz][4][1]+(__.z1carton['Widt'][iz]*0.45), ],
            [ 0 , 'L', __.z1carton['GRID'][iz][2][0]-(__.z1carton['Leng'][iz]*0.21), __.z1carton['GRID'][iz][4][1]+(__.z1carton['Widt'][iz]*0.65), ],
            [ 0 , 'L', __.z1carton['GRID'][iz][2][0]-(__.z1carton['Leng'][iz]*0.30), __.z1carton['GRID'][iz][4][1]+(__.z1carton['Widt'][iz]*0.85), ],
            [ 0 , 'L', __.z1carton['GRID'][iz][1][0]+(__.z1carton['Leng'][iz]*0.30), __.z1carton['GRID'][iz][4][1]+(__.z1carton['Widt'][iz]*0.85), ],
            [ 0 , 'L', __.z1carton['GRID'][iz][1][0]+(__.z1carton['Leng'][iz]*0.21), __.z1carton['GRID'][iz][4][1]+(__.z1carton['Widt'][iz]*0.65), ],
            [ 0 , 'L', __.z1carton['GRID'][iz][1][0]+(__.z1carton['Leng'][iz]*0.21), __.z1carton['GRID'][iz][4][1]+(__.z1carton['Widt'][iz]*0.45), ],

            [ 0 , 'L', __.z1carton['GRID'][iz][1][0], __.z1carton['GRID'][iz][4][1], ],

           ],
           'reverse':[

            [ 0x3005 ], ##------------## Lower Reverse-Side Push-Lock
            [ 0 , 'L', __.z1carton['GRID'][iz][5][0]-__._['q_tab_glue_diameter'], __.z1carton['GRID'][iz][4][1]+(__.z1carton['Leng'][iz]/2), ],
            [ 0 , 'L', __.z1carton['GRID'][iz][5][0]-(__.z1carton['Widt'][iz]/3)-__._['q_tab_glue_diameter'], __.z1carton['GRID'][iz][4][1]+(__.z1carton['Leng'][iz]/2), ],
            [ 0 , 'L', __.z1carton['GRID'][iz][5][0]-(__.z1carton['Widt'][iz]/3)-__._['q_tab_glue_diameter'], __.z1carton['GRID'][iz][4][1]+(__.z1carton['Leng'][iz]/2)-__._['q_tab_glue_diameter'], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][4][0]+3, __.z1carton['GRID'][iz][4][1]+3, ],

            [ 0 , 'L', __.z1carton['GRID'][iz][4][0], __.z1carton['GRID'][iz][4][1], ],

            [ 0 , 'L', __.z1carton['GRID'][iz][4][0]-__._['q_tab_glue_diameter'], __.z1carton['GRID'][iz][4][1]+__._['q_tab_glue_diameter'], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][4][0]-__._['q_tab_glue_diameter'], __.z1carton['GRID'][iz][4][1]+__._['q_tab_glue_diameter']+6, ],
            [ 0 , 'L', __.z1carton['GRID'][iz][4][0]-__._['q_tab_glue_diameter']-4, __.z1carton['GRID'][iz][4][1]+__._['q_tab_glue_diameter']+10, ],
            [ 0 , 'L', __.z1carton['GRID'][iz][3][0]+__._['q_tab_glue_diameter']+4, __.z1carton['GRID'][iz][4][1]+__._['q_tab_glue_diameter']+10, ],
            [ 0 , 'L', __.z1carton['GRID'][iz][3][0]+__._['q_tab_glue_diameter'], __.z1carton['GRID'][iz][4][1]+__._['q_tab_glue_diameter']+6, ],
            [ 0 , 'L', __.z1carton['GRID'][iz][3][0]+__._['q_tab_glue_diameter'], __.z1carton['GRID'][iz][4][1]+__._['q_tab_glue_diameter'], ],

            [ 0 , 'L', __.z1carton['GRID'][iz][3][0], __.z1carton['GRID'][iz][4][1], ],

            [ 0 , 'L', __.z1carton['GRID'][iz][3][0]-3, __.z1carton['GRID'][iz][4][1]+3, ],
            [ 0 , 'L', __.z1carton['GRID'][iz][2][0]+(__.z1carton['Widt'][iz]/3)+__._['q_tab_glue_diameter'], __.z1carton['GRID'][iz][4][1]+(__.z1carton['Leng'][iz]/2)-__._['q_tab_glue_diameter'], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][2][0]+(__.z1carton['Widt'][iz]/3)+__._['q_tab_glue_diameter'], __.z1carton['GRID'][iz][4][1]+(__.z1carton['Leng'][iz]/2), ],
            [ 0 , 'L', __.z1carton['GRID'][iz][2][0]+__._['q_tab_glue_diameter'], __.z1carton['GRID'][iz][4][1]+(__.z1carton['Leng'][iz]/2), ],

            [ 0 , 'L', __.z1carton['GRID'][iz][2][0], __.z1carton['GRID'][iz][4][1], ],

            [ 0 , 'L', __.z1carton['GRID'][iz][2][0]-__._['q_tab_glue_diameter'], __.z1carton['GRID'][iz][4][1]+(__.z1carton['Leng'][iz]/2), ],
            [ 0 , 'L', __.z1carton['GRID'][iz][2][0]-(__._['q_tab_glue_diameter']*1.1), __.z1carton['GRID'][iz][4][1]+(__.z1carton['Leng'][iz]/2), ],
            [ 0 , 'L', __.z1carton['GRID'][iz][2][0]-(__._['q_tab_glue_diameter']*1.1), __.z1carton['GRID'][iz][4][1]+(__.z1carton['Leng'][iz]/2)-__._['q_tab_glue_diameter'], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][1][0]+(__._['q_tab_glue_diameter']*1.1), __.z1carton['GRID'][iz][4][1]+(__.z1carton['Leng'][iz]/2)-__._['q_tab_glue_diameter'], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][1][0]+(__._['q_tab_glue_diameter']*1.1), __.z1carton['GRID'][iz][4][1]+(__.z1carton['Leng'][iz]/2), ],
            [ 0 , 'L', __.z1carton['GRID'][iz][1][0]+__._['q_tab_glue_diameter'], __.z1carton['GRID'][iz][4][1]+(__.z1carton['Leng'][iz]/2), ],

            [ 0 , 'L', __.z1carton['GRID'][iz][1][0], __.z1carton['GRID'][iz][4][1], ],

           ]

          },
          'outer-flap':{

           '0':[
           ],

          },
          'mid-flap':{

           'A':[
           ],
           'B':[
           ],

          },
          'inner-flap':{

           '0':[
           ],

          },

        }
        
        ##
        ## Generated components
        
        if __.z0job0['fullcube']=='full' and __.z1carton['Hang'][iz]=='1':
          _softcarton_['common']['hang-tab']['inner'].append([
            [ 256 ], ['q_chop_inn'],
          ])
          for qZ in range(len(__._geom_['q_hang_pin'][0])):
            _softcarton_['common']['hang-tab']['inner'].append([
              [ 0, 'M' if qZ==0 else 'L', 
              (__.z1carton['GRID'][iz][_hangoffset_+1][0]+(__.z1carton['Leng'][iz]*0.5)+__._geom_['q_hang_pin'][0][qZ]),
              (__.z1carton['GRID'][iz][2][1]-__._['q_hang_tab_height']+__._['q_hang_pin_margin']+__._geom_['q_hang_pin'][1][qZ]) ]
            ])
          _softcarton_['common']['hang-tab']['inner'].append([ [ 0, 'z' ] ]) # important! the nesting number of arrays must match the above contours!

        
        ##
        ## carton crease path
        _fold_=[
          ['q_fold_glue_tab'],
          [ [ # glue 90deg permanent fold; seam reduction is experimental and will almost certainly produce a lopsided top-end.
            [ 0x0000 ],
            [ 0 , 'M', __.z1carton['GRID'][iz][1][0]+__._['q_tab_glue_fold_reduction'], __.z1carton['GRID'][iz][2][1], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][1][0]+__._['q_tab_glue_fold_reduction'], __.z1carton['GRID'][iz][4][1], ],
          ],[
            [ 0x0018 ], # test the half-cube only feature by plotting this otherwise theoretical glue crease line only on half-cubes.
            [ 0 , 'M', __.z1carton['GRID'][iz][5][0]+__._['q_tab_glue_fold_reduction'], __.z1carton['GRID'][iz][2][1], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][5][0]+__._['q_tab_glue_fold_reduction'], __.z1carton['GRID'][iz][4][1], ],
          ] ],
          ['q_fold_base'],
          [ [ # base 90deg permanent fold; I have inverted q_crease_lid_hinge_outset because I want those extended margins factored into the grid!
            [ 0x0000 ], ## half carton
            [ 0 , 'M', __.z1carton['GRID'][iz][2][0], __.z1carton['GRID'][iz][2][1], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][2][0], __.z1carton['GRID'][iz][4][1], ],
          ],[
            [ 0x0001 ], ## full carton
            [ 1 , 'M', __.z1carton['GRID'][iz][3][0], __.z1carton['GRID'][iz][2][1], ],
            [ 1 , 'L', __.z1carton['GRID'][iz][3][0], __.z1carton['GRID'][iz][4][1], ],
            [ 1 , 'M', __.z1carton['GRID'][iz][4][0], __.z1carton['GRID'][iz][2][1], ],
            [ 1 , 'L', __.z1carton['GRID'][iz][4][0], __.z1carton['GRID'][iz][4][1], ],
          ] ],
          ['q_fold_hinge'],
          [ [ # base hinge 90deg accessable fold
            [ 0x0802 ],
            [ 0 , 'M', __.z1carton['GRID'][iz][1][0], __.z1carton['GRID'][iz][2][1]-0, ],
            [ 0 , 'L', __.z1carton['GRID'][iz][2][0], __.z1carton['GRID'][iz][2][1]-0, ], # lid upper hinge
            [ 0 , 'M', __.z1carton['GRID'][iz][2][0], __.z1carton['GRID'][iz][2][1]+__._['q_crease_lid_hinge_outset'], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][3][0], __.z1carton['GRID'][iz][2][1]+__._['q_crease_lid_hinge_outset'], ], # lid flap 1
            [ 1 , 'M', __.z1carton['GRID'][iz][4][0], __.z1carton['GRID'][iz][2][1]+__._['q_crease_lid_hinge_outset'], ],
            [ 1 , 'L', __.z1carton['GRID'][iz][5][0], __.z1carton['GRID'][iz][2][1]+__._['q_crease_lid_hinge_outset'], ], # lid flap 2
          ],[
            [ 0x2802 ],
            [ 0 , 'M', __.z1carton['GRID'][iz][2][0]+__._['q_tab_dust_seam_reduction'], __.z1carton['GRID'][iz][2][1]+__._['q_crease_lid_hinge_outset'], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][3][0], __.z1carton['GRID'][iz][2][1]+__._['q_crease_lid_hinge_outset'], ], # lid flap 1
            [ 1 , 'M', __.z1carton['GRID'][iz][3][0], __.z1carton['GRID'][iz][2][1]-0, ],
            [ 1 , 'L', __.z1carton['GRID'][iz][4][0], __.z1carton['GRID'][iz][2][1]-0, ], # lid upper hinge
            [ 1 , 'M', __.z1carton['GRID'][iz][4][0], __.z1carton['GRID'][iz][2][1]+__._['q_crease_lid_hinge_outset'], ],
            [ 1 , 'L', __.z1carton['GRID'][iz][5][0], __.z1carton['GRID'][iz][2][1]+__._['q_crease_lid_hinge_outset'], ], # lid flap 2
          ],[
            [ 0x1002 ],
            [ 1 , 'M', __.z1carton['GRID'][iz][5][0], __.z1carton['GRID'][iz][4][1]-__._['q_crease_lid_hinge_outset'], ],
            [ 1 , 'L', __.z1carton['GRID'][iz][4][0], __.z1carton['GRID'][iz][4][1]-__._['q_crease_lid_hinge_outset'], ], # base flap 2
            [ 0 , 'M', __.z1carton['GRID'][iz][3][0], __.z1carton['GRID'][iz][4][1]-__._['q_crease_lid_hinge_outset'], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][2][0], __.z1carton['GRID'][iz][4][1]-__._['q_crease_lid_hinge_outset'], ], # base flap 1
            [ 0 , 'M', __.z1carton['GRID'][iz][2][0], __.z1carton['GRID'][iz][4][1]+0, ],
            [ 0 , 'L', __.z1carton['GRID'][iz][1][0], __.z1carton['GRID'][iz][4][1]+0, ], # full cube lid lower hinge
          ],[
            [ 0x3002 ],
            [ 1 , 'M', __.z1carton['GRID'][iz][5][0], __.z1carton['GRID'][iz][4][1]-__._['q_crease_lid_hinge_outset'], ],
            [ 1 , 'L', __.z1carton['GRID'][iz][4][0], __.z1carton['GRID'][iz][4][1]-__._['q_crease_lid_hinge_outset'], ], # base flap 2
            [ 1 , 'M', __.z1carton['GRID'][iz][4][0], __.z1carton['GRID'][iz][4][1]+0, ],
            [ 1 , 'L', __.z1carton['GRID'][iz][3][0], __.z1carton['GRID'][iz][4][1]+0, ], # full cube lid lower hinge
            [ 0 , 'M', __.z1carton['GRID'][iz][3][0], __.z1carton['GRID'][iz][4][1]-__._['q_crease_lid_hinge_outset'], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][2][0]+__._['q_tab_dust_seam_reduction'], __.z1carton['GRID'][iz][4][1]-__._['q_crease_lid_hinge_outset'], ], # base flap 1
          ],[
            [ 0x1004 ],
            [ 1 , 'M', __.z1carton['GRID'][iz][5][0], __.z1carton['GRID'][iz][4][1]-0, ],
            [ 1 , 'L', __.z1carton['GRID'][iz][4][0], __.z1carton['GRID'][iz][4][1]-0, ], # base flap 2
            [ 1 , 'M', __.z1carton['GRID'][iz][4][0], __.z1carton['GRID'][iz][4][1]-__._['q_crease_lid_hinge_outset'], ],
            [ 1 , 'L', __.z1carton['GRID'][iz][3][0], __.z1carton['GRID'][iz][4][1]-__._['q_crease_lid_hinge_outset'], ], # full cube crash lower hinge
            [ 0 , 'M', __.z1carton['GRID'][iz][3][0], __.z1carton['GRID'][iz][4][1]+0, ],
            [ 0 , 'L', __.z1carton['GRID'][iz][2][0], __.z1carton['GRID'][iz][4][1]+0, ], # base flap 1
            [ 0 , 'M', __.z1carton['GRID'][iz][2][0], __.z1carton['GRID'][iz][4][1]+__._['q_crease_lid_hinge_outset'], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][1][0], __.z1carton['GRID'][iz][4][1]+__._['q_crease_lid_hinge_outset'], ], # full cube crash lower hinge
          ],[
            [ 0x3004 ],
            [ 1 , 'M', __.z1carton['GRID'][iz][5][0], __.z1carton['GRID'][iz][4][1]+0, ],
            [ 1 , 'L', __.z1carton['GRID'][iz][4][0], __.z1carton['GRID'][iz][4][1]+0, ], # base flap 2
            [ 1 , 'M', __.z1carton['GRID'][iz][4][0], __.z1carton['GRID'][iz][4][1]+__._['q_crease_lid_hinge_outset'], ],
            [ 1 , 'L', __.z1carton['GRID'][iz][3][0], __.z1carton['GRID'][iz][4][1]+__._['q_crease_lid_hinge_outset'], ], # full cube crash lower hinge
            [ 0 , 'M', __.z1carton['GRID'][iz][3][0], __.z1carton['GRID'][iz][4][1]-0, ],
            [ 0 , 'L', __.z1carton['GRID'][iz][2][0], __.z1carton['GRID'][iz][4][1]-0, ], # base flap 1
            [ 0 , 'M', __.z1carton['GRID'][iz][2][0], __.z1carton['GRID'][iz][4][1]-__._['q_crease_lid_hinge_outset'], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][1][0], __.z1carton['GRID'][iz][4][1]-__._['q_crease_lid_hinge_outset'], ], # full cube crash lower hinge
          ] ],
          ['q_fold_lid_tab'],
          [ [ # lid hinge 90deg accessable fold
            [ 0x0802 ],
            [ 0 , 'M', __.z1carton['GRID'][iz][1][0]+__._['q_tab_lid_flap_line'], __.z1carton['GRID'][iz][1][1]+__._['q_crease_lid_flap_inset'], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][2][0]-__._['q_tab_lid_flap_line'], __.z1carton['GRID'][iz][1][1]+__._['q_crease_lid_flap_inset'], ], # lid tab hinge
          ],[
            [ 0x2803 ],
            [ 0 , 'M', __.z1carton['GRID'][iz][3][0]+__._['q_tab_lid_flap_line'], __.z1carton['GRID'][iz][1][1]+__._['q_crease_lid_flap_inset'], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][4][0]-__._['q_tab_lid_flap_line'], __.z1carton['GRID'][iz][1][1]+__._['q_crease_lid_flap_inset'], ], # lid tab hinge
          ],[
            [ 0x3003 ],
            [ 0 , 'M', __.z1carton['GRID'][iz][4][0]-__._['q_tab_lid_flap_line'], __.z1carton['GRID'][iz][5][1]-__._['q_crease_lid_flap_inset'], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][3][0]+__._['q_tab_lid_flap_line'], __.z1carton['GRID'][iz][5][1]-__._['q_crease_lid_flap_inset'], ], # full cube lid tab hinge
          ],[
            [ 0x1002 ],
            [ 0 , 'M', __.z1carton['GRID'][iz][2][0]-__._['q_tab_lid_flap_line'], __.z1carton['GRID'][iz][5][1]-__._['q_crease_lid_flap_inset'], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][1][0]+__._['q_tab_lid_flap_line'], __.z1carton['GRID'][iz][5][1]-__._['q_crease_lid_flap_inset'], ], # full cube lid tab hinge
          ] ],
        ]

          #[
          #  #### topcap (not enabled) ####
          #  [ 0x1005 ], # Cap the top while detail is under development
          #  [ 0 , 'M', __.z1carton['GRID'][iz][1][0], __.z1carton['GRID'][iz][2][1]+(4), ],
          #  [ 0 , 'L', __.z1carton['GRID'][iz][5][0], __.z1carton['GRID'][iz][2][1]+(4), ],
          #],[
          #  #### potcap (not enabled) ####
          #  [ 0x3005 ], # Cap the pot while detail is under development
          #  [ 0 , 'M', __.z1carton['GRID'][iz][5][0], __.z1carton['GRID'][iz][4][1]-(4), ],
          #  [ 0 , 'L', __.z1carton['GRID'][iz][1][0], __.z1carton['GRID'][iz][4][1]-(4), ],
          #],

        ##
        ## carton closed and open paths
        _chop_=[

##------------## Closed Path ##----##
         ['q_diagnose'], [

          # This is the right side of the carton. This initial move is now redundant
          # in this case where components have been offloaded into arrays and functions.
          [ [ 0 , 'M', __.z1carton['GRID'][iz][1][0]-(0), __.z1carton['GRID'][iz][2][1]-(0), ], ],
          [ [ 0 , 'M', __.z1carton['GRID'][iz][1][0]-(4), __.z1carton['GRID'][iz][2][1]-(4), ], ],
          
##------------## Lid
          ##------------## Upper Forward-Side Clip-Lock
          ], ['q_chop_out_flap_out'], [
          _softcarton_['cliplock']['outer-flap']['A1'],
          ], ['q_chop_out_flap_inn'], [
          _softcarton_['cliplock']['inner-flap']['A1i1'],_softcarton_['cliplock']['inner-flap']['A1o1'],
          ], ['q_chop_out_basewall'], [
          _softcarton_['cliplock']['outer-edge']['A1'], 
          ], ['q_chop_out_flap_inn'], [
          _softcarton_['cliplock']['inner-flap']['A1i2'],_softcarton_['cliplock']['inner-flap']['A1o2'],

          ##------------## Upper Reverse-Side Clip-Lock
          ], ['q_chop_out_basewall'], [
          _softcarton_['cliplock']['outer-edge']['A2'], 
          ], ['q_chop_out_flap_inn'], [
          _softcarton_['cliplock']['inner-flap']['A2i1'],_softcarton_['cliplock']['inner-flap']['A2o1'],
          ], ['q_chop_out_flap_out'], [
          _softcarton_['cliplock']['outer-flap']['A2'], 
          ], ['q_chop_out_flap_inn'], [
          _softcarton_['cliplock']['inner-flap']['A2i2'],_softcarton_['cliplock']['inner-flap']['A2o2'],

##------------## Right Wall
          ], ['q_chop_out_sidewall'], [
          [
            [ 0x0001 ], # This is the right side of the carton.
            [ 0 , 'M', __.z1carton['GRID'][iz][5][0], __.z1carton['GRID'][iz][2][1], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][5][0], __.z1carton['GRID'][iz][4][1], ],
          ],[
            [ 0x0008 ], # This is the right side of the carton.
            [ 0 , 'M', __.z1carton['GRID'][iz][3][0], __.z1carton['GRID'][iz][2][1], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][3][0], __.z1carton['GRID'][iz][4][1], ],
          ],

          #_softcarton_['common']['glue-tab']['R'],

##------------## Base
          ##------------## Lower Forward-Side Clip-Lock
          ], ['q_chop_out_flap_inn'], [
          _softcarton_['cliplock']['inner-flap']['B1i1'],_softcarton_['cliplock']['inner-flap']['B1o1'],
          ], ['q_chop_out_basewall'], [
          _softcarton_['cliplock']['outer-edge']['B1'], 
          ], ['q_chop_out_flap_inn'], [
          _softcarton_['cliplock']['inner-flap']['B1i2'],_softcarton_['cliplock']['inner-flap']['B1o2'],
          ], ['q_chop_out_flap_out'], [
          _softcarton_['cliplock']['outer-flap']['B1'],
          
          ##------------## Lower Reverse-Side Clip-Lock
          ], ['q_chop_out_flap_inn'], [
          _softcarton_['cliplock']['inner-flap']['B2i1'],_softcarton_['cliplock']['inner-flap']['B2o1'],
          ], ['q_chop_out_flap_out'], [
          _softcarton_['cliplock']['outer-flap']['B2'],
          ], ['q_chop_out_flap_inn'], [
          _softcarton_['cliplock']['inner-flap']['B2i2'],_softcarton_['cliplock']['inner-flap']['B2o2'],
          ], ['q_chop_out_basewall'], [
          _softcarton_['cliplock']['outer-edge']['B2'], 

          ], ['q_chop_out'], [
          ##------------## Lower Forward-Side Push-Lock
          _softcarton_['pushlock']['onepiece']['forward'],
          ##------------## Lower Reverse-Side Push-Lock
          _softcarton_['pushlock']['onepiece']['reverse'],

##------------## Left Wall
          ], ['q_chop_out_sidewall'], [
          [
            [ 0x0010 ], # This is the left side of the carton.
            [ 0 , 'M', __.z1carton['GRID'][iz][3][0]-4, __.z1carton['GRID'][iz][4][1]-4, ],
            [ 0 , 'L', __.z1carton['GRID'][iz][3][0]+4, __.z1carton['GRID'][iz][4][1]+4, ],
              # end the outline for a full cube only, and begin again remaining half cube ready outlines.
              # #8 is for squaring off a half cube only; do not show it on the full flatpack outline.
          ],
          _softcarton_['common']['glue-tab']['L'],
          
##------------## Close our Closed Path ##====##

##------------## Open Path ##----##
          ], ['q_chop_inn_tab'], [
          [
##------------## Lid Flap Notch
            [ 0x0802 ], # the remainder of this brace will be flagged as lid-geometry.
            [ 0 , 'M', __.z1carton['GRID'][iz][1][0], __.z1carton['GRID'][iz][1][1], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][1][0]+__._['q_tab_lid_flap_line'], __.z1carton['GRID'][iz][1][1], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][1][0]+__._['q_tab_lid_flap_line'], __.z1carton['GRID'][iz][1][1]+__._['q_tab_lid_flap_hook'], ],
            [ 0 , 'M', __.z1carton['GRID'][iz][2][0], __.z1carton['GRID'][iz][1][1], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][2][0]-__._['q_tab_lid_flap_line'], __.z1carton['GRID'][iz][1][1], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][2][0]-__._['q_tab_lid_flap_line'], __.z1carton['GRID'][iz][1][1]+__._['q_tab_lid_flap_hook'], ],
          ],[
            [ 0x2803 ], # the remainder of this brace will be flagged as lid-geometry.
            [ 0 , 'M', __.z1carton['GRID'][iz][3][0], __.z1carton['GRID'][iz][1][1], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][3][0]+__._['q_tab_lid_flap_line'], __.z1carton['GRID'][iz][1][1], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][3][0]+__._['q_tab_lid_flap_line'], __.z1carton['GRID'][iz][1][1]+__._['q_tab_lid_flap_hook'], ],
            [ 0 , 'M', __.z1carton['GRID'][iz][4][0], __.z1carton['GRID'][iz][1][1], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][4][0]-__._['q_tab_lid_flap_line'], __.z1carton['GRID'][iz][1][1], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][4][0]-__._['q_tab_lid_flap_line'], __.z1carton['GRID'][iz][1][1]+__._['q_tab_lid_flap_hook'], ],
          ],[
##------------## Base Flap Notch
            [ 0x1002 ], # the remainder of this brace will be flagged as base-geometry.
            [ 0 , 'M', __.z1carton['GRID'][iz][2][0], __.z1carton['GRID'][iz][5][1], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][2][0]-__._['q_tab_lid_flap_line'], __.z1carton['GRID'][iz][5][1], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][2][0]-__._['q_tab_lid_flap_line'], __.z1carton['GRID'][iz][5][1]-__._['q_tab_lid_flap_hook'], ],
            [ 0 , 'M', __.z1carton['GRID'][iz][1][0], __.z1carton['GRID'][iz][5][1], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][1][0]+__._['q_tab_lid_flap_line'], __.z1carton['GRID'][iz][5][1], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][1][0]+__._['q_tab_lid_flap_line'], __.z1carton['GRID'][iz][5][1]-__._['q_tab_lid_flap_hook'], ],
          ],[
            [ 0x3003 ], # the remainder of this brace will be flagged as base-geometry.
            [ 0 , 'M', __.z1carton['GRID'][iz][4][0], __.z1carton['GRID'][iz][5][1], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][4][0]-__._['q_tab_lid_flap_line'], __.z1carton['GRID'][iz][5][1], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][4][0]-__._['q_tab_lid_flap_line'], __.z1carton['GRID'][iz][5][1]-__._['q_tab_lid_flap_hook'], ],
            [ 0 , 'M', __.z1carton['GRID'][iz][3][0], __.z1carton['GRID'][iz][5][1], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][3][0]+__._['q_tab_lid_flap_line'], __.z1carton['GRID'][iz][5][1], ],
            [ 0 , 'L', __.z1carton['GRID'][iz][3][0]+__._['q_tab_lid_flap_line'], __.z1carton['GRID'][iz][5][1]-__._['q_tab_lid_flap_hook'], ],
          ],
          ], ['q_chop_inn_hang'], [
##------------## Hanging Eyelet
          _softcarton_['common']['hang-tab']['inner'], # eyelet cutout for a point-of-sale rack mounted hanger
##------------## EndOf our Open Paths ##====##
          ],
        ]
        
        ##
        ## window
        _window_chop=[]
        for qZ in range(len(__.z1carton['Window'][iz]['centre']['x'])):
          ##
          ## carton openings (windows)
          if (
            (__.z1carton['Window'][iz]['Xi'][qZ]>0 and __.z1carton['Window'][iz]['Yi'][qZ]>0)
            and not (qZ==5 and __.z1carton['Base'][iz]!='c-lock')
          ):
            _window_chop.append([
              [ 128 ], ['q_chop_inn_window'],
              [ 0, 'M', __.z1carton['Window'][iz]['centre']['x'][qZ]-(__.z1carton['Window'][iz]['Xi'][qZ]/2)+(__.z1carton['Window'][iz]['Curved'][qZ]),
                        __.z1carton['Window'][iz]['centre']['y'][qZ]-(__.z1carton['Window'][iz]['Yi'][qZ]/2), ],
              [ 0, 'L', __.z1carton['Window'][iz]['centre']['x'][qZ]+(__.z1carton['Window'][iz]['Xi'][qZ]/2)-(__.z1carton['Window'][iz]['Curved'][qZ]),
                        __.z1carton['Window'][iz]['centre']['y'][qZ]-(__.z1carton['Window'][iz]['Yi'][qZ]/2), ],
                [ 0, 'C', 
                          __.z1carton['Window'][iz]['centre']['x'][qZ]+(__.z1carton['Window'][iz]['Xi'][qZ]/2)-(__.z1carton['Window'][iz]['Curved'][qZ]/2),
                          __.z1carton['Window'][iz]['centre']['y'][qZ]-(__.z1carton['Window'][iz]['Yi'][qZ]/2),
                          __.z1carton['Window'][iz]['centre']['x'][qZ]+(__.z1carton['Window'][iz]['Xi'][qZ]/2),
                          __.z1carton['Window'][iz]['centre']['y'][qZ]-(__.z1carton['Window'][iz]['Yi'][qZ]/2)+(__.z1carton['Window'][iz]['Curved'][qZ]/2),
                          __.z1carton['Window'][iz]['centre']['x'][qZ]+(__.z1carton['Window'][iz]['Xi'][qZ]/2),
                          __.z1carton['Window'][iz]['centre']['y'][qZ]-(__.z1carton['Window'][iz]['Yi'][qZ]/2)+(__.z1carton['Window'][iz]['Curved'][qZ]),
                ],
              [ 0, 'L', __.z1carton['Window'][iz]['centre']['x'][qZ]+(__.z1carton['Window'][iz]['Xi'][qZ]/2),
                        __.z1carton['Window'][iz]['centre']['y'][qZ]+(__.z1carton['Window'][iz]['Yi'][qZ]/2)-(__.z1carton['Window'][iz]['Curved'][qZ]), ],
                [ 0, 'C', 
                          __.z1carton['Window'][iz]['centre']['x'][qZ]+(__.z1carton['Window'][iz]['Xi'][qZ]/2),
                          __.z1carton['Window'][iz]['centre']['y'][qZ]+(__.z1carton['Window'][iz]['Yi'][qZ]/2)-(__.z1carton['Window'][iz]['Curved'][qZ]/2),
                          __.z1carton['Window'][iz]['centre']['x'][qZ]+(__.z1carton['Window'][iz]['Xi'][qZ]/2)-(__.z1carton['Window'][iz]['Curved'][qZ]/2),
                          __.z1carton['Window'][iz]['centre']['y'][qZ]+(__.z1carton['Window'][iz]['Yi'][qZ]/2),
                          __.z1carton['Window'][iz]['centre']['x'][qZ]+(__.z1carton['Window'][iz]['Xi'][qZ]/2)-(__.z1carton['Window'][iz]['Curved'][qZ]),
                          __.z1carton['Window'][iz]['centre']['y'][qZ]+(__.z1carton['Window'][iz]['Yi'][qZ]/2),
                ],
              [ 0, 'L', __.z1carton['Window'][iz]['centre']['x'][qZ]-(__.z1carton['Window'][iz]['Xi'][qZ]/2)+(__.z1carton['Window'][iz]['Curved'][qZ]),
                        __.z1carton['Window'][iz]['centre']['y'][qZ]+(__.z1carton['Window'][iz]['Yi'][qZ]/2), ],
                [ 0, 'C', 
                          __.z1carton['Window'][iz]['centre']['x'][qZ]-(__.z1carton['Window'][iz]['Xi'][qZ]/2)+(__.z1carton['Window'][iz]['Curved'][qZ]/2),
                          __.z1carton['Window'][iz]['centre']['y'][qZ]+(__.z1carton['Window'][iz]['Yi'][qZ]/2),
                          __.z1carton['Window'][iz]['centre']['x'][qZ]-(__.z1carton['Window'][iz]['Xi'][qZ]/2),
                          __.z1carton['Window'][iz]['centre']['y'][qZ]+(__.z1carton['Window'][iz]['Yi'][qZ]/2)-(__.z1carton['Window'][iz]['Curved'][qZ]/2),
                          __.z1carton['Window'][iz]['centre']['x'][qZ]-(__.z1carton['Window'][iz]['Xi'][qZ]/2),
                          __.z1carton['Window'][iz]['centre']['y'][qZ]+(__.z1carton['Window'][iz]['Yi'][qZ]/2)-(__.z1carton['Window'][iz]['Curved'][qZ]),
                ],
              [ 0, 'L', __.z1carton['Window'][iz]['centre']['x'][qZ]-(__.z1carton['Window'][iz]['Xi'][qZ]/2),
                        __.z1carton['Window'][iz]['centre']['y'][qZ]-(__.z1carton['Window'][iz]['Yi'][qZ]/2)+(__.z1carton['Window'][iz]['Curved'][qZ]), ],
                [ 0, 'C', 
                          __.z1carton['Window'][iz]['centre']['x'][qZ]-(__.z1carton['Window'][iz]['Xi'][qZ]/2),
                          __.z1carton['Window'][iz]['centre']['y'][qZ]-(__.z1carton['Window'][iz]['Yi'][qZ]/2)+(__.z1carton['Window'][iz]['Curved'][qZ]/2),
                          __.z1carton['Window'][iz]['centre']['x'][qZ]-(__.z1carton['Window'][iz]['Xi'][qZ]/2)+(__.z1carton['Window'][iz]['Curved'][qZ]/2),
                          __.z1carton['Window'][iz]['centre']['y'][qZ]-(__.z1carton['Window'][iz]['Yi'][qZ]/2),
                          __.z1carton['Window'][iz]['centre']['x'][qZ]-(__.z1carton['Window'][iz]['Xi'][qZ]/2)+(__.z1carton['Window'][iz]['Curved'][qZ]),
                          __.z1carton['Window'][iz]['centre']['y'][qZ]-(__.z1carton['Window'][iz]['Yi'][qZ]/2),
                ],
              #[ 0, 'z', ],
            ])
        __.z1carton['PlanWindow'][iz] = [ _window_chop ]

        ##
        ## insert
        _insert_fold=[]
        _insert_chop=[]
        for qZ in range(len(__.z1carton['GridInsert'][iz])): #(__.z1carton['GridInsert'][iz].buffer_info()[1]):
          ##
          ## insert crease path
          if (__.z1carton['Insert'][iz]['Li'][qZ]>0 and __.z1carton['Insert'][iz]['Wi'][qZ]>0 and __.z1carton['Insert'][iz]['Hi'][qZ]>0):
            _insert_fold.append([
              [ 512 ], ['q_fold_insert'],
              [ 0, 'M', __.z1carton['GridInsert'][iz][qZ][0],
                        __.z1carton['GridInsert'][iz][qZ][1]+__.z1carton['Insert'][iz]['Hi'][qZ], ],
              [ 0, 'L', __.z1carton['GridInsert'][iz][qZ][0]+__.z1carton['Insert'][iz]['Li'][qZ],
                        __.z1carton['GridInsert'][iz][qZ][1]+__.z1carton['Insert'][iz]['Hi'][qZ], ],
              [ 0, 'M', __.z1carton['GridInsert'][iz][qZ][0],
                        __.z1carton['GridInsert'][iz][qZ][1]+__.z1carton['Insert'][iz]['Hi'][qZ]+__.z1carton['Insert'][iz]['Wi'][qZ], ],
              [ 0, 'L', __.z1carton['GridInsert'][iz][qZ][0]+__.z1carton['Insert'][iz]['Li'][qZ],
                        __.z1carton['GridInsert'][iz][qZ][1]+__.z1carton['Insert'][iz]['Hi'][qZ]+__.z1carton['Insert'][iz]['Wi'][qZ], ],
              [ 0, 'M', __.z1carton['GridInsert'][iz][qZ][0],
                        __.z1carton['GridInsert'][iz][qZ][1]+(__.z1carton['Insert'][iz]['Hi'][qZ]*2)+__.z1carton['Insert'][iz]['Wi'][qZ], ],
              [ 0, 'L', __.z1carton['GridInsert'][iz][qZ][0]+__.z1carton['Insert'][iz]['Li'][qZ],
                        __.z1carton['GridInsert'][iz][qZ][1]+(__.z1carton['Insert'][iz]['Hi'][qZ]*2)+__.z1carton['Insert'][iz]['Wi'][qZ], ],
              [ 0, 'M', __.z1carton['GridInsert'][iz][qZ][0],
                        __.z1carton['GridInsert'][iz][qZ][1]+(__.z1carton['Insert'][iz]['Hi'][qZ]*2)+(__.z1carton['Insert'][iz]['Wi'][qZ]*2), ],
              [ 0, 'L', __.z1carton['GridInsert'][iz][qZ][0]+__.z1carton['Insert'][iz]['Li'][qZ],
                        __.z1carton['GridInsert'][iz][qZ][1]+(__.z1carton['Insert'][iz]['Hi'][qZ]*2)+(__.z1carton['Insert'][iz]['Wi'][qZ]*2), ],
            ])
          ##
          ## insert closed path
            _insert_chop.append([
              [ 512 ], ['q_chop_out_insert'],
              [ 0 , 'M', __.z1carton['GridInsert'][iz][qZ][0],
                         __.z1carton['GridInsert'][iz][qZ][1], ],
              [ 0 , 'L', __.z1carton['GridInsert'][iz][qZ][0]+__.z1carton['Insert'][iz]['Li'][qZ],
                         __.z1carton['GridInsert'][iz][qZ][1], ],
              [ 0 , 'L', __.z1carton['GridInsert'][iz][qZ][0]+__.z1carton['Insert'][iz]['Li'][qZ],
                         __.z1carton['GridInsert'][iz][qZ][1]+(__.z1carton['Insert'][iz]['Hi'][qZ]*2)+(__.z1carton['Insert'][iz]['Wi'][qZ]*2), ],
              [ 0 , 'L', __.z1carton['GridInsert'][iz][qZ][0]+__.z1carton['Insert'][iz]['Li'][qZ]-__._['q_tab_glue_taper'],
                         __.z1carton['GridInsert'][iz][qZ][1]+(__.z1carton['Insert'][iz]['Hi'][qZ]*2)+(__.z1carton['Insert'][iz]['Wi'][qZ]*2)+__._['q_tab_glue_diameter'], ],
              [ 0 , 'L', __.z1carton['GridInsert'][iz][qZ][0]+__._['q_tab_glue_taper'],
                         __.z1carton['GridInsert'][iz][qZ][1]+(__.z1carton['Insert'][iz]['Hi'][qZ]*2)+(__.z1carton['Insert'][iz]['Wi'][qZ]*2)+__._['q_tab_glue_diameter'], ],
              [ 0 , 'L', __.z1carton['GridInsert'][iz][qZ][0],
                         __.z1carton['GridInsert'][iz][qZ][1]+(__.z1carton['Insert'][iz]['Hi'][qZ]*2)+(__.z1carton['Insert'][iz]['Wi'][qZ]*2), ],
              [ 0 , 'z', ],
            ])
          ##
          ## insert open paths
          ##https://www.linux-magazine.com/Issues/2020/239/Magic-Circle
          attribs = {
            'style': str(_inx.Style(__._stylesheet_['q_chop_inn_insert'])),
            _inx.addNS('label', 'inkscape'): "myinsert01slot",
            'cx': str(__.z1carton['GridInsert'][iz][qZ][0]+(__.z1carton['Insert'][iz]['Li'][qZ]*0.5)),
            'cy': str(__.z1carton['GridInsert'][iz][qZ][1]+(__.z1carton['Insert'][iz]['Wi'][qZ]*0.5)+__.z1carton['Insert'][iz]['Hi'][qZ]),
            'r': str(__.z1carton['Insert'][iz]['Ba'][qZ])
          }
          #if __.z1carton['Insert'][iz]['Ba'][qZ]>0:
          #  __._page_.add(_inx.Circle (**attribs))
        __.z1carton['PlanInsert'][iz] = [ _insert_fold, _insert_chop ]

        __.z1carton['PLAN'][iz]= _fold_ + _chop_ + __.z1carton['PlanWindow'][iz] + __.z1carton['PlanInsert'][iz]

    def uffect_1(__, list00): # 1 piece
      iz=0
      #__.groupindex=0
      # All three .set()s following must be used together to maintain scale!!!
      xx= __.z1carton['GRID'][iz][ len(__.z1carton['GRID'][iz])-1 ][0] + (2*__.z1carton['GRID'][iz][0][0])
      yy= __.z1carton['GRID'][iz][ len(__.z1carton['GRID'][iz])-1 ][1] + (2*__.z1carton['GRID'][iz][0][1])
      __._root_.set('width',str(xx)+"mm")
      __._root_.set('height',str(yy)+"mm")
      __._root_.set('viewBox', '0 0 %.0f %.0f' % (xx, yy))
      for iz in range(len(__.z1carton['Enable'])):
      #  ##https://inkscape.org/forums/extensions/extension-access-children-of-layer/
      #  ##https://github.com/wvengen/inkscape-addons/blob/master/extensions/multi_page_pdf_output.py
      #  _l_fold=__._page_
      #  _l_chop=__._page_
      #  for layer in __.svg:
      #    if layer.label=="fold":
      #      _l_fold=layer
      #    if layer.label=="chop":
      #      _l_chop=layer
      #    if layer.label == "fold" or layer.label == "chop":
      #      #__.msg("Walls")
      #      for node in layer:
      #        wall = {"width":node.width,"height":node.height, "x":node.left, "y":node.top}
      #        #__.msg(_j.dumps(wall))
      #        if (__.debug[0]): _inx.utils.debug(wall)

        if (__.debug[0] or __.debug[1]):
          _inx.utils.debug([ '__01pc: ', iz, '__Enable: ', __.z1carton['Enable'][iz] ])
        # ( boolean parameters need to have been parsed as strings to work as intended! )
        if( __.z1carton['Enable'][iz]=='true' ):
        
          scanstring='item-{0:d}'.format(iz) # We are immediately pruning something. Today it is going to be what was immediately generated prior.
          #scanstring='prior-{0:d}'.format(iz) # in future, I shall give the operator one opportunity to save their prior work if it is wanted.
          for element in __._root_.iter(tag=_x.Element):
            if element.eid[0:len(scanstring)]==scanstring: # 
              #for child in element.getchildren(): # Redundant; inkscape already seems to throw out the babies with the bathwater for us.
              #  element.remove(child)
              element.getparent().remove(element) # Prior work is no longer wanted! Remove this pollution from our XML SVG namespace!
              pass

          # This next part is intended to preserve the pre-existing layers that will later be pruned above.
          # I have disabled it, for although it does not commit any data I have not applied previously,
          # it crashes Inkscape. Inkscape does not seem to like renaming elements in this manner,
          # or perhaps it might have something to do with name collisions.
          
          #for element in __._root_.iter(tag=_x.Element): # Here is where we provide that one opportunity to preserve the old work.
          #  if (
          #    element.eid[0:6]=='regi-{0:d}'.format(iz) or
          #    element.eid[0:6]=='diag-{0:d}'.format(iz) or
          #    element.eid[0:6]=='fold-{0:d}'.format(iz) or
          #    element.eid[0:6]=='chop-{0:d}'.format(iz) or
          #  True ):
          #    element.set('id', 'prior-{0:s}'.format(element.eid))
          #    pass

          __.uffect_0( __.z1carton['PLAN'][iz], iz ) # dielines

      __.iffect_1( {} ) # registration



    def offect_2(__): # 2 piece
      for iz in range(len(__.z2rigbox['Enable'])):
        pass

    def uffect_2(__, list00): # 2 piece
      for iz in range(len(__.z2rigbox['Enable'])):
        __.uffect_0( __.z2rigbox['PLAN'], iz )



    def offect_3(__): # Insert
        # insert offset geometry
        __.z3insert['GRID']=[
          [ __.z0job0['offset'][0][0], __.z0job0['offset'][0][1] ],
        ]
        for qZ in range( 1, len(__.z3insert['Li']) ):
          __.z3insert['GRID'].append(
            [ __.z0job0['offset'][0][0] +
              __.z3insert['GRID'][qZ-1][0]+
              __.z3insert['Li'][qZ-1],
              __.z0job0['offset'][0][1] ],
          )
        ##
        ## insert
        _insert_fold=[]
        _insert_chop=[]
        for qZ in range( len(__.z3insert['GRID']) ): #(__.z3insert['GRID'].buffer_info()[1]):
          ##
          ## insert crease path
          if (__.z3insert['Li'][qZ]>0 and __.z3insert['Wi'][qZ]>0 and __.z3insert['Hi'][qZ]>0):
            EE=[
              (1 if __._['q_03in_'+str(qZ)+'E1']>0 else 0)+
              (1 if __._['q_03in_'+str(qZ)+'E2']>0 else 0),
              __._['q_03in_'+str(qZ)+'E1'],
              __._['q_03in_'+str(qZ)+'E2'],
            ]
            _insert_fold.append([
              [ 512 ], ['q_fold_insert'],
              [ 0, 'M', __.z3insert['GRID'][qZ][0],
                        __.z3insert['GRID'][qZ][1]+__.z3insert['Hi'][qZ], ],
              [ 0, 'L', __.z3insert['GRID'][qZ][0]+__.z3insert['Li'][qZ],
                        __.z3insert['GRID'][qZ][1]+__.z3insert['Hi'][qZ], ],
              [ 0, 'M', __.z3insert['GRID'][qZ][0],
                        __.z3insert['GRID'][qZ][1]+__.z3insert['Hi'][qZ]+__.z3insert['Wi'][qZ], ],
              [ 0, 'L', __.z3insert['GRID'][qZ][0]+__.z3insert['Li'][qZ],
                        __.z3insert['GRID'][qZ][1]+__.z3insert['Hi'][qZ]+__.z3insert['Wi'][qZ], ],
              [ 0, 'M', __.z3insert['GRID'][qZ][0],
                        __.z3insert['GRID'][qZ][1]+(__.z3insert['Hi'][qZ]*2)+__.z3insert['Wi'][qZ], ],
              [ 0, 'L', __.z3insert['GRID'][qZ][0]+__.z3insert['Li'][qZ],
                        __.z3insert['GRID'][qZ][1]+(__.z3insert['Hi'][qZ]*2)+__.z3insert['Wi'][qZ], ],
              [ 0, 'M', __.z3insert['GRID'][qZ][0],
                        __.z3insert['GRID'][qZ][1]+(__.z3insert['Hi'][qZ]*2)+(__.z3insert['Wi'][qZ]*2), ],
              [ 0, 'L', __.z3insert['GRID'][qZ][0]+__.z3insert['Li'][qZ],
                        __.z3insert['GRID'][qZ][1]+(__.z3insert['Hi'][qZ]*2)+(__.z3insert['Wi'][qZ]*2), ],
            ])
            if (EE[1]>0):
              _insert_fold.append([
              [ 0, 'M', __.z3insert['GRID'][qZ][0],
                        __.z3insert['GRID'][qZ][1]+
                        (__.z3insert['Hi'][qZ]*2)+
                        (__.z3insert['Wi'][qZ]*2)+
                        EE[1], ],
              [ 0, 'L', __.z3insert['GRID'][qZ][0]+__.z3insert['Li'][qZ],
                        __.z3insert['GRID'][qZ][1]+
                        (__.z3insert['Hi'][qZ]*2)+
                        (__.z3insert['Wi'][qZ]*2)+
                        EE[1], ],
              [ 0, 'M', __.z3insert['GRID'][qZ][0],
                        __.z3insert['GRID'][qZ][1]+
                        (__.z3insert['Hi'][qZ]*2)+
                        (__.z3insert['Wi'][qZ]*3)+
                        EE[1], ],
              [ 0, 'L', __.z3insert['GRID'][qZ][0]+__.z3insert['Li'][qZ],
                        __.z3insert['GRID'][qZ][1]+
                        (__.z3insert['Hi'][qZ]*2)+
                        (__.z3insert['Wi'][qZ]*3)+
                        EE[1], ],
              ])
            if (EE[2]>0):
              _insert_fold.append([
              [ 0, 'M', __.z3insert['GRID'][qZ][0],
                        __.z3insert['GRID'][qZ][1]+
                        (__.z3insert['Hi'][qZ]*2)+
                        (__.z3insert['Wi'][qZ]*3)+
                        EE[1]+EE[2], ],
              [ 0, 'L', __.z3insert['GRID'][qZ][0]+__.z3insert['Li'][qZ],
                        __.z3insert['GRID'][qZ][1]+
                        (__.z3insert['Hi'][qZ]*2)+
                        (__.z3insert['Wi'][qZ]*3)+
                        EE[1]+EE[2], ],
              [ 0, 'M', __.z3insert['GRID'][qZ][0],
                        __.z3insert['GRID'][qZ][1]+
                        (__.z3insert['Hi'][qZ]*2)+
                        (__.z3insert['Wi'][qZ]*4)+
                        EE[1]+EE[2], ],
              [ 0, 'L', __.z3insert['GRID'][qZ][0]+__.z3insert['Li'][qZ],
                        __.z3insert['GRID'][qZ][1]+
                        (__.z3insert['Hi'][qZ]*2)+
                        (__.z3insert['Wi'][qZ]*4)+
                        EE[1]+EE[2], ],
              ])
          ##
          ## insert closed path
            _insert_chop.append([
              [ 512 ], ['q_chop_out_insert'],
              [ 0 , 'M', __.z3insert['GRID'][qZ][0],
                         __.z3insert['GRID'][qZ][1], ],
              [ 0 , 'L', __.z3insert['GRID'][qZ][0]+__.z3insert['Li'][qZ],
                         __.z3insert['GRID'][qZ][1], ],
              [ 0 , 'L', __.z3insert['GRID'][qZ][0]+__.z3insert['Li'][qZ],
                         __.z3insert['GRID'][qZ][1]+EE[1]+EE[2]+
                         (__.z3insert['Hi'][qZ]*2)+
                         (__.z3insert['Wi'][qZ]* (2+EE[0]) ), ],
              [ 0 , 'L', __.z3insert['GRID'][qZ][0]+
                         __.z3insert['Li'][qZ]-__._['q_tab_glue_taper'],
                         __.z3insert['GRID'][qZ][1]+EE[1]+EE[2]+
                         (__.z3insert['Hi'][qZ]*2)+
                         (__.z3insert['Wi'][qZ]* (2+EE[0]) )+__._['q_tab_glue_diameter'], ],
              [ 0 , 'L', __.z3insert['GRID'][qZ][0]+__._['q_tab_glue_taper'],
                         __.z3insert['GRID'][qZ][1]+EE[1]+EE[2]+
                         (__.z3insert['Hi'][qZ]*2)+
                         (__.z3insert['Wi'][qZ]* (2+EE[0]) )+__._['q_tab_glue_diameter'], ],
              [ 0 , 'L', __.z3insert['GRID'][qZ][0],
                         __.z3insert['GRID'][qZ][1]+EE[1]+EE[2]+
                         (__.z3insert['Hi'][qZ]*2)+
                         (__.z3insert['Wi'][qZ]* (2+EE[0]) ), ],
              [ 0 , 'z', ],
            ])
            #if (EE[1]>0):
            #  _insert_chop.append([
            #  ])
            #if (EE[2]>0):
            #  _insert_chop.append([
            #  ])
          ##
          ## insert open paths
          ##https://www.linux-magazine.com/Issues/2020/239/Magic-Circle
          attribs = {
            'style': str(_inx.Style(__._stylesheet_['q_chop_inn'])),
            _inx.addNS('label', 'inkscape'): "myinsert01slot",
            'cx': str(__.z3insert['GRID'][qZ][0]+(__.z3insert['Li'][qZ]*0.5)),
            'cy': str(__.z3insert['GRID'][qZ][1]+(__.z3insert['Wi'][qZ]*0.5)+__.z3insert['Hi'][qZ]),
            'r': str(__.z3insert['Ba'][qZ])
          }
          #if __.z3insert['Ba'][qZ]>0:
          #  __._page_.add(_inx.Circle (**attribs))
        __.z3insert['PLAN'] = [ _insert_fold, _insert_chop ]

    def uffect_3(__, list00): # Insert
        qZ=0
        # All three .set()s following must be used together to maintain scale!!!
        xx= (__.z0job0['offset'][qZ][0]*2) + __.z3insert['Li'][qZ]
        yy= (__.z0job0['offset'][qZ][1]*2) + ( ( __.z3insert['Hi'][qZ] + __.z3insert['Wi'][qZ] )*2 )+__._['q_tab_glue_diameter']
        __._root_.set('width',str(xx)+"mm")
        __._root_.set('height',str(yy)+"mm")
        __._root_.set('viewBox', '0 0 %.0f %.0f' % (xx, yy))

        __.uffect_0( __.z3insert['PLAN'], 0 )



    def offect_4(__): # Imposition
        pass

    def uffect_4(__, list00):
        __.uffect_0( __.z4impose['PLAN'], 0 )
    

    
    def offect_5(__): # Outset / Container
        # slottedcontainer offset geometry
        __.z5outset['GRID']=[\
          [__.z0job0['offset'][0][0], __.z0job0['offset'][0][1]], \
        ]

        for qZ in range(len(__.z5outset['GRID'])):
         ##
         ## flap
         __.z5outset['FlapHeight'][qZ]=(
           (__.z5outset['Len'][qZ]/2) if
           (__.z5outset['Len'][qZ]/2) < (__.z5outset['Wid'][qZ]) else
           (__.z5outset['Wid'][qZ]/1)
         )
         for zZ in range(int(__.z5outset['Quantity'][qZ])):
          qZdeep, qZflap= float(__.z5outset['Height'][qZ]), __.z5outset['FlapHeight'][qZ] #__.z5outset['Wid'][qZ]/2 #__.z1carton['GRID'][7][1]/2
          qZdeeper=((qZflap*2)+qZdeep)*zZ
          ##
          ## slottedcontainer crease path
          sP={}
          sP['61']=[
            [ 1024 ], [ 'q_fold_outset' ],
            [ 1024, 'M', __.z5outset['GRID'][qZ][0]+__.z5outset['Len'][qZ], __.z5outset['GRID'][qZ][1]+qZflap+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+__.z5outset['Len'][qZ], __.z5outset['GRID'][qZ][1]+qZflap+qZdeep+qZdeeper ],
            [ 1024, 'M', __.z5outset['GRID'][qZ][0]+__.z5outset['Len'][qZ]+__.z5outset['Wid'][qZ], __.z5outset['GRID'][qZ][1]+qZflap+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+__.z5outset['Len'][qZ]+__.z5outset['Wid'][qZ], __.z5outset['GRID'][qZ][1]+qZflap+qZdeep+qZdeeper ],
            [ 1024, 'M', __.z5outset['GRID'][qZ][0]+(__.z5outset['Len'][qZ]*2)+__.z5outset['Wid'][qZ], __.z5outset['GRID'][qZ][1]+qZflap+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+(__.z5outset['Len'][qZ]*2)+__.z5outset['Wid'][qZ], __.z5outset['GRID'][qZ][1]+qZflap+qZdeep+qZdeeper ],
            [ 1024, 'M', __.z5outset['GRID'][qZ][0]+(__.z5outset['Len'][qZ]+__.z5outset['Wid'][qZ])*2, __.z5outset['GRID'][qZ][1]+qZflap+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+(__.z5outset['Len'][qZ]+__.z5outset['Wid'][qZ])*2, __.z5outset['GRID'][qZ][1]+qZflap+qZdeep+qZdeeper ],
            [ 1024, 'M', __.z5outset['GRID'][qZ][0]+0, __.z5outset['GRID'][qZ][1]+qZflap-1+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+__.z5outset['Len'][qZ], __.z5outset['GRID'][qZ][1]+qZflap-1+qZdeeper ],
            [ 1024, 'M', __.z5outset['GRID'][qZ][0]+__.z5outset['Len'][qZ], __.z5outset['GRID'][qZ][1]+qZflap+1+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+__.z5outset['Len'][qZ]+__.z5outset['Wid'][qZ], __.z5outset['GRID'][qZ][1]+qZflap+1+qZdeeper ],
            [ 1024, 'M', __.z5outset['GRID'][qZ][0]+__.z5outset['Len'][qZ]+__.z5outset['Wid'][qZ], __.z5outset['GRID'][qZ][1]+qZflap-1+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+(__.z5outset['Len'][qZ]*2)+__.z5outset['Wid'][qZ], __.z5outset['GRID'][qZ][1]+qZflap-1+qZdeeper ],
            [ 1024, 'M', __.z5outset['GRID'][qZ][0]+(__.z5outset['Len'][qZ]*2)+__.z5outset['Wid'][qZ], __.z5outset['GRID'][qZ][1]+qZflap+1+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+(__.z5outset['Len'][qZ]+__.z5outset['Wid'][qZ])*2, __.z5outset['GRID'][qZ][1]+qZflap+1+qZdeeper ],
            [ 1024, 'M', __.z5outset['GRID'][qZ][0]+0, __.z5outset['GRID'][qZ][1]+qZflap+qZdeep+1+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+__.z5outset['Len'][qZ], __.z5outset['GRID'][qZ][1]+qZflap+qZdeep+1+qZdeeper ],
            [ 1024, 'M', __.z5outset['GRID'][qZ][0]+__.z5outset['Len'][qZ], __.z5outset['GRID'][qZ][1]+qZflap+qZdeep-1+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+__.z5outset['Len'][qZ]+__.z5outset['Wid'][qZ], __.z5outset['GRID'][qZ][1]+qZflap+qZdeep-1+qZdeeper ],
            [ 1024, 'M', __.z5outset['GRID'][qZ][0]+__.z5outset['Len'][qZ]+__.z5outset['Wid'][qZ], __.z5outset['GRID'][qZ][1]+qZflap+qZdeep+1+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+(__.z5outset['Len'][qZ]*2)+__.z5outset['Wid'][qZ], __.z5outset['GRID'][qZ][1]+qZflap+qZdeep+1+qZdeeper ],
            [ 1024, 'M', __.z5outset['GRID'][qZ][0]+(__.z5outset['Len'][qZ]*2)+__.z5outset['Wid'][qZ], __.z5outset['GRID'][qZ][1]+qZflap+qZdeep-1+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+(__.z5outset['Len'][qZ]+__.z5outset['Wid'][qZ])*2, __.z5outset['GRID'][qZ][1]+qZflap+qZdeep-1+qZdeeper ],
          ]
          ##
          ## slottedcontainer closed path
          sP['72']=[
            [ 1024 ], [ 'q_chop_out_outset' ],
            [ 1024, ' ', __.z5outset['GRID'][qZ][0]+(__.z5outset['Len'][qZ]+__.z5outset['Wid'][qZ])*2-1.5, __.z5outset['GRID'][qZ][1]+0+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+(__.z5outset['Len'][qZ]+__.z5outset['Wid'][qZ])*2-1.5, __.z5outset['GRID'][qZ][1]+qZflap+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+(__.z5outset['Len'][qZ]+__.z5outset['Wid'][qZ])*2, __.z5outset['GRID'][qZ][1]+qZflap+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+20+(__.z5outset['Len'][qZ]+__.z5outset['Wid'][qZ])*2, __.z5outset['GRID'][qZ][1]+qZflap+10+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+20+(__.z5outset['Len'][qZ]+__.z5outset['Wid'][qZ])*2, __.z5outset['GRID'][qZ][1]+qZflap+qZdeep-10+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+(__.z5outset['Len'][qZ]+__.z5outset['Wid'][qZ])*2, __.z5outset['GRID'][qZ][1]+qZflap+qZdeep+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+(__.z5outset['Len'][qZ]+__.z5outset['Wid'][qZ])*2-1.5, __.z5outset['GRID'][qZ][1]+qZflap+qZdeep+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+(__.z5outset['Len'][qZ]+__.z5outset['Wid'][qZ])*2-1.5, __.z5outset['GRID'][qZ][1]+(qZflap*2)+qZdeep+qZdeeper ],
          ]
          sP['73']=[
            [ 1024 ], [ 'q_chop_out_outset' ],
            [ 1024, ' ', __.z5outset['GRID'][qZ][0]+(__.z5outset['Len'][qZ]*2)+__.z5outset['Wid'][qZ]+1.5, __.z5outset['GRID'][qZ][1]+(qZflap*2)+qZdeep+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+(__.z5outset['Len'][qZ]*2)+__.z5outset['Wid'][qZ]+1.5, __.z5outset['GRID'][qZ][1]+qZflap+qZdeep+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+(__.z5outset['Len'][qZ]*2)+__.z5outset['Wid'][qZ]-1.5, __.z5outset['GRID'][qZ][1]+qZflap+qZdeep+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+(__.z5outset['Len'][qZ]*2)+__.z5outset['Wid'][qZ]-1.5, __.z5outset['GRID'][qZ][1]+(qZflap*2)+qZdeep+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+__.z5outset['Len'][qZ]+__.z5outset['Wid'][qZ]+1.5, __.z5outset['GRID'][qZ][1]+(qZflap*2)+qZdeep+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+__.z5outset['Len'][qZ]+__.z5outset['Wid'][qZ]+1.5, __.z5outset['GRID'][qZ][1]+qZflap+qZdeep+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+__.z5outset['Len'][qZ]+__.z5outset['Wid'][qZ]-1.5, __.z5outset['GRID'][qZ][1]+qZflap+qZdeep+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+__.z5outset['Len'][qZ]+__.z5outset['Wid'][qZ]-1.5, __.z5outset['GRID'][qZ][1]+(qZflap*2)+qZdeep+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+__.z5outset['Len'][qZ]+1.5, __.z5outset['GRID'][qZ][1]+(qZflap*2)+qZdeep+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+__.z5outset['Len'][qZ]+1.5, __.z5outset['GRID'][qZ][1]+qZflap+qZdeep+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+__.z5outset['Len'][qZ]-1.5, __.z5outset['GRID'][qZ][1]+qZflap+qZdeep+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+__.z5outset['Len'][qZ]-1.5, __.z5outset['GRID'][qZ][1]+(qZflap*2)+qZdeep+qZdeeper ],
          ]
          sP['74']=[
            [ 1024 ], [ 'q_chop_out_outset' ],
            [ 1024, ' ', __.z5outset['GRID'][qZ][0]+1.5, __.z5outset['GRID'][qZ][1]+(qZflap*2)+qZdeep+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+1.5, __.z5outset['GRID'][qZ][1]+qZflap+qZdeep+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0], __.z5outset['GRID'][qZ][1]+qZflap+qZdeep+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0], __.z5outset['GRID'][qZ][1]+qZflap+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+1.5, __.z5outset['GRID'][qZ][1]+qZflap+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+1.5, __.z5outset['GRID'][qZ][1]+0+qZdeeper ],
          ]
          sP['75']=[
            [ 1024 ], [ 'q_chop_out_outset' ],
            [ 1024, ' ', __.z5outset['GRID'][qZ][0]+__.z5outset['Len'][qZ]-1.5, __.z5outset['GRID'][qZ][1]+0+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+__.z5outset['Len'][qZ]-1.5, __.z5outset['GRID'][qZ][1]+qZflap+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+__.z5outset['Len'][qZ]+1.5, __.z5outset['GRID'][qZ][1]+qZflap+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+__.z5outset['Len'][qZ]+1.5, __.z5outset['GRID'][qZ][1]+0+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+__.z5outset['Len'][qZ]+__.z5outset['Wid'][qZ]-1.5, __.z5outset['GRID'][qZ][1]+0+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+__.z5outset['Len'][qZ]+__.z5outset['Wid'][qZ]-1.5, __.z5outset['GRID'][qZ][1]+qZflap+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+__.z5outset['Len'][qZ]+__.z5outset['Wid'][qZ]+1.5, __.z5outset['GRID'][qZ][1]+qZflap+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+__.z5outset['Len'][qZ]+__.z5outset['Wid'][qZ]+1.5, __.z5outset['GRID'][qZ][1]+0+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+(__.z5outset['Len'][qZ]*2)+__.z5outset['Wid'][qZ]-1.5, __.z5outset['GRID'][qZ][1]+0+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+(__.z5outset['Len'][qZ]*2)+__.z5outset['Wid'][qZ]-1.5, __.z5outset['GRID'][qZ][1]+qZflap+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+(__.z5outset['Len'][qZ]*2)+__.z5outset['Wid'][qZ]+1.5, __.z5outset['GRID'][qZ][1]+qZflap+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+(__.z5outset['Len'][qZ]*2)+__.z5outset['Wid'][qZ]+1.5, __.z5outset['GRID'][qZ][1]+0+qZdeeper ],
          ]
          sP['85']=[
            [ 1024 ], [ 'q_chop_out_outset' ],
            [ 1024, ' ', __.z5outset['GRID'][qZ][0]+1.5, __.z5outset['GRID'][qZ][1]+0+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+__.z5outset['Len'][qZ]-1.5, __.z5outset['GRID'][qZ][1]+0+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+__.z5outset['Len'][qZ]-1.5, __.z5outset['GRID'][qZ][1]-qZflap+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+__.z5outset['Len'][qZ]-1.5, __.z5outset['GRID'][qZ][1]+qZflap+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+__.z5outset['Len'][qZ]+1.5, __.z5outset['GRID'][qZ][1]+qZflap+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+__.z5outset['Len'][qZ]+1.5, __.z5outset['GRID'][qZ][1]-qZflap+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+__.z5outset['Len'][qZ]-1.5, __.z5outset['GRID'][qZ][1]-qZflap+qZdeeper ],
            [ 1024, 'M', __.z5outset['GRID'][qZ][0]+__.z5outset['Len'][qZ]+1.5, __.z5outset['GRID'][qZ][1]+0+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+__.z5outset['Len'][qZ]+__.z5outset['Wid'][qZ]-1.5, __.z5outset['GRID'][qZ][1]+0+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+__.z5outset['Len'][qZ]+__.z5outset['Wid'][qZ]-1.5, __.z5outset['GRID'][qZ][1]-qZflap+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+__.z5outset['Len'][qZ]+__.z5outset['Wid'][qZ]-1.5, __.z5outset['GRID'][qZ][1]+qZflap+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+__.z5outset['Len'][qZ]+__.z5outset['Wid'][qZ]+1.5, __.z5outset['GRID'][qZ][1]+qZflap+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+__.z5outset['Len'][qZ]+__.z5outset['Wid'][qZ]+1.5, __.z5outset['GRID'][qZ][1]-qZflap+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+__.z5outset['Len'][qZ]+__.z5outset['Wid'][qZ]-1.5, __.z5outset['GRID'][qZ][1]-qZflap+qZdeeper ],
            [ 1024, 'M', __.z5outset['GRID'][qZ][0]+__.z5outset['Len'][qZ]+__.z5outset['Wid'][qZ]+1.5, __.z5outset['GRID'][qZ][1]+0+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+(__.z5outset['Len'][qZ]*2)+__.z5outset['Wid'][qZ]-1.5, __.z5outset['GRID'][qZ][1]+0+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+(__.z5outset['Len'][qZ]*2)+__.z5outset['Wid'][qZ]-1.5, __.z5outset['GRID'][qZ][1]-qZflap+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+(__.z5outset['Len'][qZ]*2)+__.z5outset['Wid'][qZ]-1.5, __.z5outset['GRID'][qZ][1]+qZflap+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+(__.z5outset['Len'][qZ]*2)+__.z5outset['Wid'][qZ]+1.5, __.z5outset['GRID'][qZ][1]+qZflap+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+(__.z5outset['Len'][qZ]*2)+__.z5outset['Wid'][qZ]+1.5, __.z5outset['GRID'][qZ][1]-qZflap+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+(__.z5outset['Len'][qZ]*2)+__.z5outset['Wid'][qZ]-1.5, __.z5outset['GRID'][qZ][1]-qZflap+qZdeeper ],
            [ 1024, 'M', __.z5outset['GRID'][qZ][0]+(__.z5outset['Len'][qZ]*2)+__.z5outset['Wid'][qZ]+1.5, __.z5outset['GRID'][qZ][1]+0+qZdeeper ],
            [ 1024, 'L', __.z5outset['GRID'][qZ][0]+(__.z5outset['Len'][qZ]+__.z5outset['Wid'][qZ])*2-1.5, __.z5outset['GRID'][qZ][1]+0+qZdeeper ],
          ]
          sP['88']=[
            [ 1024 ], [ 'q_chop_out_outset' ],
            [ 1024, 'z' ],
          ]

          sP['60']=[ sP['61'] ]
          if zZ>0:
            if zZ>=int(__.z5outset['Quantity'][qZ])-1:
              sP['70']=[ sP['72'], sP['73'], sP['74'] ] #'M'+sP72+'L'+sP73+'L'+sP74 # 3/3
              sP['80']=[ sP['85'] ] #'M'+sP85 # 2/3
              sP['70'][0][2][1]='M'
              sP['70'][1][2][1]='L'
              sP['70'][2][2][1]='L'
              sP['80'][0][2][1]='M'
            else:
              sP['70']=[ sP['72'], sP['74'] ] #'M'+sP72+'M'+sP74 # 2/3
              sP['80']=[ sP['85'] ] #'M'+sP85 # 2/3
              sP['70'][0][2][1]='M'
              sP['70'][1][2][1]='M'
              sP['80'][0][2][1]='M'
          else:
            if int(__.z5outset['Quantity'][qZ])>1:
              sP['70']=[ sP['74'], sP['75'], sP['72'] ] #'M'+sP74+'L'+sP75+'L'+sP72 # 1/3
              sP['80']=[]
              sP['70'][0][2][1]='M'
              sP['70'][1][2][1]='L'
              sP['70'][2][2][1]='L'
            else:
              sP['70']=[ sP['72'], sP['73'], sP['74'], sP['75'], sP['88'] ] #'M'+sP72+'L'+sP73+'L'+sP74+'L'+sP75+'z' # 1/1
              sP['80']=[]
              sP['70'][0][2][1]='M'
              sP['70'][1][2][1]='L'
              sP['70'][2][2][1]='L'
              sP['70'][3][2][1]='L'

          #__.z5outset['PLAN'].append([ sP['60'], sP['70'], sP['80'] ])
          __.z5outset['PLAN'].append( sP['60'] )
          __.z5outset['PLAN'].append( sP['70'] )
          __.z5outset['PLAN'].append( sP['80'] )
          if __.debug[0]:
            _inx.utils.debug('________________')
            _inx.utils.debug(',<'+sP['60'].__str__()+'>')
            _inx.utils.debug(',<'+sP['70'].__str__()+'>')
            _inx.utils.debug(',<'+sP['80'].__str__()+'>')
            _inx.utils.debug('----------------')

    def uffect_5(__, list00):
        qZ=0
        #zZ=int(__.z5outset['Quantity'][qZ])-1
        #qZdeep, qZflap= float(__.z5outset['Height'][qZ]), __.z5outset['Wid'][qZ]/2
        #qZdeeper=((qZflap*2)+qZdeep)*zZ
        # All three .set()s following must be used together to maintain scale!!!
        xx= __.z5outset['GRID'][qZ][0] + ( ( __.z5outset['Len'][qZ] + __.z5outset['Wid'][qZ] )*2 ) + (20) + ( __.z0job0['offset'][0][0]*1 )
        yy= __.z5outset['GRID'][qZ][1] + ( ( __.z5outset['Wid'][qZ] + float(__.z5outset['Height'][qZ]) ) * int(__.z5outset['Quantity'][qZ]) ) + ( __.z0job0['offset'][0][1]*1 )
        __._root_.set('width',str(xx)+"mm")
        __._root_.set('height',str(yy)+"mm")
        __._root_.set('viewBox', '0 0 %.0f %.0f' % (xx, yy))
        ##https://inkscape.org/forums/extensions/extension-access-children-of-layer/
        ##https://github.com/wvengen/inkscape-addons/blob/master/extensions/multi_page_pdf_output.py

        __.uffect_0( __.z5outset['PLAN'], 0 )



    def offect_6(__): # Palletization
        pass

    def uffect_6(__, list00):
        __.uffect_0( __.z6pallet['PLAN'], 0 )



    def offect(__):
        #if len(__.svg.selected) == 0:
        #    sys.exit(_gt_("Error: You must select at least one path"))
    
        ##https://wiki.inkscape.org/wiki/Generating_objects_from_extensions
        # modified for Inkscape UI upgrade from 0.92 to 1.12
        __._page_ = __.svg.get_current_layer()
        style = {
          'stroke'        : '#E0E0E0',
          'stroke-width'  : '12',
          'fill'          : '#404040'
        }		        
        attribs = {
          'style'     : str(_inx.Style(style)),
          'height'    : str(64),
          'width'     : str(64),
          'x'         : str(__._['q_0all_origin_x']),
          'y'         : str(__._['q_0all_origin_y'])
        }
        ####square = _x.SubElement(__._page_, _inx.addNS('rect','svg'), attribs )
        style = {
          'stroke': '#C0E0C0',
          'stroke-width':'3',
          'fill': '#808080'
        }
        attribs = {
          'style' : str(_inx.Style(style)),
          _inx.addNS('label','inkscape') : "myline",
          'd' : 'M '+
          str(__._['q_0all_origin_x']+8)+','+str(__._['q_0all_origin_y']+8)+
          ' L '+
          str(__._['q_0all_origin_x']+60)+','+str(__._['q_0all_origin_y']+60)
        }
        ####line = _x.SubElement(__._page_, _inx.addNS('path','svg'), attribs )



    def add_arguments(__, pars):
        'Process program parameters passed in from the UI.'
        
        #'Tab'
        pars.add_argument('--tab0', dest='tab', help='This was the selected UI tab when OK was pressed')

        #'WigIt'
        pars.add_argument('--historyfader01', type=int, help='Transition between current and former drawing via translucency values')
        
        #'ClickIt'
        ##  OK BUTTON HERE  ##

# analysis #1: default settings
        pars.add_argument('--z_0all_c', type=str, help='') # global settings

        pars.add_argument('--debug0', type=int, help='debug0')
        pars.add_argument('--debug1', type=int, help='debug1')
        pars.add_argument('--debug2', type=int, help='debug0')
        pars.add_argument('--debug3', type=int, help='debug1')

        pars.add_argument('--q_c_contact1', type=str, help='')
        pars.add_argument('--q_c_contact2', type=str, help='')
        pars.add_argument('--q_c_contact3', type=str, help='')
        pars.add_argument('--q_c_contact4', type=str, help='')

        pars.add_argument('--q_col1_cre1', type=_inx.Color, default=_inx.Color("white"), help='')
        pars.add_argument('--q_col1_cre4', type=_inx.Color, default=_inx.Color("white"), help='')
        pars.add_argument('--q_col1_cre5', type=_inx.Color, default=_inx.Color("white"), help='')
        pars.add_argument('--q_col1_cre6', type=_inx.Color, default=_inx.Color("white"), help='')
        pars.add_argument('--q_col1_cre7', type=_inx.Color, default=_inx.Color("white"), help='')
        pars.add_argument('--q_col1_cre8', type=_inx.Color, default=_inx.Color("white"), help='')
        pars.add_argument('--q_col1_cre9', type=_inx.Color, default=_inx.Color("white"), help='')
        pars.add_argument('--q_col1_creA', type=_inx.Color, default=_inx.Color("white"), help='')
        pars.add_argument('--q_col1_cut1', type=_inx.Color, default=_inx.Color("white"), help='')
        pars.add_argument('--q_col1_cut4', type=_inx.Color, default=_inx.Color("white"), help='')
        pars.add_argument('--q_col1_cut5', type=_inx.Color, default=_inx.Color("white"), help='')
        pars.add_argument('--q_col1_cut6', type=_inx.Color, default=_inx.Color("white"), help='')
        pars.add_argument('--q_col1_cut7', type=_inx.Color, default=_inx.Color("white"), help='')
        pars.add_argument('--q_col1_cut8', type=_inx.Color, default=_inx.Color("white"), help='')
        pars.add_argument('--q_col1_cut9', type=_inx.Color, default=_inx.Color("white"), help='')
        pars.add_argument('--q_col1_cutA', type=_inx.Color, default=_inx.Color("white"), help='')
        pars.add_argument('--q_col1_cutB', type=_inx.Color, default=_inx.Color("white"), help='')
        pars.add_argument('--q_col1_cutC', type=_inx.Color, default=_inx.Color("white"), help='')
        pars.add_argument('--q_col1_cutD', type=_inx.Color, default=_inx.Color("white"), help='')
        pars.add_argument('--q_col1_cutE', type=_inx.Color, default=_inx.Color("white"), help='')
        pars.add_argument('--q_col1_cutF', type=_inx.Color, default=_inx.Color("white"), help='')
        pars.add_argument('--q_col1_cutG', type=_inx.Color, default=_inx.Color("white"), help='')
        pars.add_argument('--q_col1_cutH', type=_inx.Color, default=_inx.Color("white"), help='')
        pars.add_argument('--q_col1_reg1', type=_inx.Color, default=_inx.Color("white"), help='')
        pars.add_argument('--q_col1_reg4', type=_inx.Color, default=_inx.Color("white"), help='')
        pars.add_argument('--q_col1_dia1', type=_inx.Color, default=_inx.Color("white"), help='')
        pars.add_argument('--q_col1_dia4', type=_inx.Color, default=_inx.Color("white"), help='')
        pars.add_argument('--q_col2_cre1', type=_inx.Color, default=_inx.Color("black"), help='')
        pars.add_argument('--q_col2_cre4', type=_inx.Color, default=_inx.Color("black"), help='')
        pars.add_argument('--q_col2_cut1', type=_inx.Color, default=_inx.Color("black"), help='')
        pars.add_argument('--q_col2_cut4', type=_inx.Color, default=_inx.Color("black"), help='')
        pars.add_argument('--q_col2_reg1', type=_inx.Color, default=_inx.Color("black"), help='')
        pars.add_argument('--q_col2_reg4', type=_inx.Color, default=_inx.Color("black"), help='')
        pars.add_argument('--q_col2_dia1', type=_inx.Color, default=_inx.Color("black"), help='')
        pars.add_argument('--q_col2_dia4', type=_inx.Color, default=_inx.Color("black"), help='')
        pars.add_argument('--q_col1_cre2', type=float, default=1.00, help='')
        pars.add_argument('--q_col1_cre3', type=float, default=1.00, help='')
        pars.add_argument('--q_col1_cut2', type=float, default=0.25, help='')
        pars.add_argument('--q_col1_cut3', type=float, default=1.00, help='')
        pars.add_argument('--q_col1_reg2', type=float, default=1.00, help='')
        pars.add_argument('--q_col1_reg3', type=float, default=1.00, help='')
        pars.add_argument('--q_col1_dia2', type=float, default=3.00, help='')
        pars.add_argument('--q_col1_dia3', type=float, default=1.00, help='')
        pars.add_argument('--q_col2_cre2', type=float, default=1.00, help='')
        pars.add_argument('--q_col2_cre3', type=float, default=1.00, help='')
        pars.add_argument('--q_col2_cut2', type=float, default=0.25, help='')
        pars.add_argument('--q_col2_cut3', type=float, default=1.00, help='')
        pars.add_argument('--q_col2_reg2', type=float, default=1.00, help='')
        pars.add_argument('--q_col2_reg3', type=float, default=1.00, help='')
        pars.add_argument('--q_col2_dia2', type=float, default=3.00, help='')
        pars.add_argument('--q_col2_dia3', type=float, default=1.00, help='')

# analysis #2: job settings
        pars.add_argument('--z_0job_c', type=str, help='') # job settings

        pars.add_argument('--q_00dognum_01user', type=str, help='Job Number')
        pars.add_argument('--q_00catnum_02user', type=str, help='Catalogue Alphanumeric')
        pars.add_argument('--q_00desnum_03user', type=str, help='Design Number')
        pars.add_argument('--q_00kninum_04user', type=str, help='Knife Alphanumeric')

        pars.add_argument('--q_tab_glue_diameter', type=float, help='')
        pars.add_argument('--q_tab_glue_taper', type=float, help='')
        pars.add_argument('--q_tab_glue_fold_reduction', type=float, help='')
        pars.add_argument('--q_tab_glue_seam_reduction', type=float, help='')
        pars.add_argument('--q_tab_dust_flap_reduction', type=float, help='')
        pars.add_argument('--q_tab_dust_seam_reduction', type=float, help='')
        pars.add_argument('--q_hang_tab_height', type=float, help='')
        pars.add_argument('--q_hang_pin_margin', type=float, help='')

        pars.add_argument('--q_tab_lid_diameter', type=float, help='')
        pars.add_argument('--q_tab_lid_taper', type=float, help='')
        pars.add_argument('--q_tab_lid_curve_diameter', type=float, help='')
        pars.add_argument('--q_tab_lid_curve_taper', type=float, help='')
        pars.add_argument('--q_tab_lid_reduce', type=float, help='')
        pars.add_argument('--q_tab_dust_reduce', type=float, help='')
        pars.add_argument('--q_tab_lid_flap_line', type=float, help='')
        pars.add_argument('--q_tab_lid_flap_hook', type=float, help='')
        pars.add_argument('--q_crease_lid_hinge_outset', type=float, help='')
        pars.add_argument('--q_crease_lid_flap_inset', type=float, help='')

        pars.add_argument('--q_zipp_buckle_major_parallel', type=float, help='')
        pars.add_argument('--q_zipp_buckle_minor_diagonal', type=float, help='')
        pars.add_argument('--q_zipp_buckle_up_spacing', type=float, help='')
        pars.add_argument('--q_zipp_buckle_dn_spacing', type=float, help='')
        pars.add_argument('--q_push_gap_major_axis', type=float, help='')
        pars.add_argument('--q_push_gap_minor_axis', type=float, help='')

        pars.add_argument('--q_0all_medium_type', type=str, help='')
        pars.add_argument('--q_0all_medium_cali', type=str, help='')
        pars.add_argument('--q_0all_medium_x', type=float, help='media size X')
        pars.add_argument('--q_0all_medium_y', type=float, help='media size Y')
        pars.add_argument('--q_0all_origin_x', type=float, help='draw offset')
        pars.add_argument('--q_0all_origin_y', type=float, help='')
        pars.add_argument('--q_0all_offset_x', type=float, help='next offset')
        pars.add_argument('--q_0all_offset_y', type=float, help='')
        pars.add_argument('--q_0all_area_amount', type=str, help='Draw a Half or Full Cube')
        pars.add_argument('--q_0all_grid_type', type=str, help='Components Grid')
        pars.add_argument('--q_0all_plot_register', type=str, help='Registration Marks')
        pars.add_argument('--q_0all_measure_absolute', type=str, help='')
        pars.add_argument('--q_0all_measure_relative', type=str, help='')

# design #1: soft carton
        pars.add_argument('--z_01pc_c', type=str, help='') # soft
        pars.add_argument('--z_01pc_u1_g', type=str, help='')
        pars.add_argument('--z_01pc_u2_g', type=str, help='')

        pars.add_argument('--q_01pc_u1_enable', type=str, help='')

        pars.add_argument('--q_01pc_u1_00L', type=float, help='L')
        pars.add_argument('--q_01pc_u1_00W', type=float, help='W')
        pars.add_argument('--q_01pc_u1_00H', type=float, help='H')
        pars.add_argument('--q_01pc_u1_00_lidd', type=str, help='lid')
        pars.add_argument('--q_01pc_u1_00_base', type=str, help='base')
        pars.add_argument('--q_01pc_u1_00_lidd_o', type=str, help='lid-orient')
        pars.add_argument('--q_01pc_u1_00_base_o', type=str, help='base-orient')
        pars.add_argument('--q_01pc_u1_00_hang', type=int, help='hang')
        pars.add_argument('--q_01pc_u1_00_flap', type=int, help='flap')

        pars.add_argument('--q_01pc_u1_window_001', type=float, help='L')
        pars.add_argument('--q_01pc_u1_window_002', type=float, help='H')
        pars.add_argument('--q_01pc_u1_window_003', type=float, help='C')
        pars.add_argument('--q_01pc_u1_window_011', type=float, help='Loff')
        pars.add_argument('--q_01pc_u1_window_012', type=float, help='Hoff')
        pars.add_argument('--q_01pc_u1_window_013', type=float, help='Anch')
        pars.add_argument('--q_01pc_u1_window_101', type=float, help='')
        pars.add_argument('--q_01pc_u1_window_102', type=float, help='')
        pars.add_argument('--q_01pc_u1_window_103', type=float, help='')
        pars.add_argument('--q_01pc_u1_window_111', type=float, help='')
        pars.add_argument('--q_01pc_u1_window_112', type=float, help='')
        pars.add_argument('--q_01pc_u1_window_113', type=float, help='')
        pars.add_argument('--q_01pc_u1_window_201', type=float, help='')
        pars.add_argument('--q_01pc_u1_window_202', type=float, help='')
        pars.add_argument('--q_01pc_u1_window_203', type=float, help='')
        pars.add_argument('--q_01pc_u1_window_211', type=float, help='')
        pars.add_argument('--q_01pc_u1_window_212', type=float, help='')
        pars.add_argument('--q_01pc_u1_window_213', type=float, help='')
        pars.add_argument('--q_01pc_u1_window_301', type=float, help='')
        pars.add_argument('--q_01pc_u1_window_302', type=float, help='')
        pars.add_argument('--q_01pc_u1_window_303', type=float, help='')
        pars.add_argument('--q_01pc_u1_window_311', type=float, help='')
        pars.add_argument('--q_01pc_u1_window_312', type=float, help='')
        pars.add_argument('--q_01pc_u1_window_313', type=float, help='')
        pars.add_argument('--q_01pc_u1_window_401', type=float, help='')
        pars.add_argument('--q_01pc_u1_window_402', type=float, help='')
        pars.add_argument('--q_01pc_u1_window_403', type=float, help='')
        pars.add_argument('--q_01pc_u1_window_411', type=float, help='')
        pars.add_argument('--q_01pc_u1_window_412', type=float, help='')
        pars.add_argument('--q_01pc_u1_window_413', type=float, help='')
        pars.add_argument('--q_01pc_u1_window_501', type=float, help='')
        pars.add_argument('--q_01pc_u1_window_502', type=float, help='')
        pars.add_argument('--q_01pc_u1_window_503', type=float, help='')
        pars.add_argument('--q_01pc_u1_window_511', type=float, help='')
        pars.add_argument('--q_01pc_u1_window_512', type=float, help='')
        pars.add_argument('--q_01pc_u1_window_513', type=float, help='')

        pars.add_argument('--q_01pc_u1_insert_001', type=float, help='L')
        pars.add_argument('--q_01pc_u1_insert_002', type=float, help='W')
        pars.add_argument('--q_01pc_u1_insert_003', type=float, help='H')
        pars.add_argument('--q_01pc_u1_insert_011', type=float, help='Aper')
        pars.add_argument('--q_01pc_u1_insert_012', type=float, help='Anch')
        pars.add_argument('--q_01pc_u1_insert_013', type=float, help='Groo')
        pars.add_argument('--q_01pc_u1_insert_101', type=float, help='')
        pars.add_argument('--q_01pc_u1_insert_102', type=float, help='')
        pars.add_argument('--q_01pc_u1_insert_103', type=float, help='')
        pars.add_argument('--q_01pc_u1_insert_111', type=float, help='')
        pars.add_argument('--q_01pc_u1_insert_112', type=float, help='')
        pars.add_argument('--q_01pc_u1_insert_113', type=float, help='')
        pars.add_argument('--q_01pc_u1_insert_201', type=float, help='')
        pars.add_argument('--q_01pc_u1_insert_202', type=float, help='')
        pars.add_argument('--q_01pc_u1_insert_203', type=float, help='')
        pars.add_argument('--q_01pc_u1_insert_211', type=float, help='')
        pars.add_argument('--q_01pc_u1_insert_212', type=float, help='')
        pars.add_argument('--q_01pc_u1_insert_213', type=float, help='')
        pars.add_argument('--q_01pc_u1_insert_301', type=float, help='')
        pars.add_argument('--q_01pc_u1_insert_302', type=float, help='')
        pars.add_argument('--q_01pc_u1_insert_303', type=float, help='')
        pars.add_argument('--q_01pc_u1_insert_311', type=float, help='')
        pars.add_argument('--q_01pc_u1_insert_312', type=float, help='')
        pars.add_argument('--q_01pc_u1_insert_313', type=float, help='')

        pars.add_argument('--q_01pc_u2_enable', type=str, help='')

        pars.add_argument('--q_01pc_u2_00L', type=float, help='L')
        pars.add_argument('--q_01pc_u2_00W', type=float, help='W')
        pars.add_argument('--q_01pc_u2_00H', type=float, help='H')
        pars.add_argument('--q_01pc_u2_00_lidd', type=str, help='lid')
        pars.add_argument('--q_01pc_u2_00_base', type=str, help='base')
        pars.add_argument('--q_01pc_u2_00_lidd_o', type=str, help='lid-orient')
        pars.add_argument('--q_01pc_u2_00_base_o', type=str, help='base-orient')
        pars.add_argument('--q_01pc_u2_00_hang', type=int, help='hang')
        pars.add_argument('--q_01pc_u2_00_flap', type=int, help='flap')

        pars.add_argument('--q_01pc_u2_window_001', type=float, help='L')
        pars.add_argument('--q_01pc_u2_window_002', type=float, help='H')
        pars.add_argument('--q_01pc_u2_window_003', type=float, help='C')
        pars.add_argument('--q_01pc_u2_window_011', type=float, help='Loff')
        pars.add_argument('--q_01pc_u2_window_012', type=float, help='Hoff')
        pars.add_argument('--q_01pc_u2_window_013', type=float, help='Anch')
        pars.add_argument('--q_01pc_u2_window_101', type=float, help='')
        pars.add_argument('--q_01pc_u2_window_102', type=float, help='')
        pars.add_argument('--q_01pc_u2_window_103', type=float, help='')
        pars.add_argument('--q_01pc_u2_window_111', type=float, help='')
        pars.add_argument('--q_01pc_u2_window_112', type=float, help='')
        pars.add_argument('--q_01pc_u2_window_113', type=float, help='')
        pars.add_argument('--q_01pc_u2_window_201', type=float, help='')
        pars.add_argument('--q_01pc_u2_window_202', type=float, help='')
        pars.add_argument('--q_01pc_u2_window_203', type=float, help='')
        pars.add_argument('--q_01pc_u2_window_211', type=float, help='')
        pars.add_argument('--q_01pc_u2_window_212', type=float, help='')
        pars.add_argument('--q_01pc_u2_window_213', type=float, help='')
        pars.add_argument('--q_01pc_u2_window_301', type=float, help='')
        pars.add_argument('--q_01pc_u2_window_302', type=float, help='')
        pars.add_argument('--q_01pc_u2_window_303', type=float, help='')
        pars.add_argument('--q_01pc_u2_window_311', type=float, help='')
        pars.add_argument('--q_01pc_u2_window_312', type=float, help='')
        pars.add_argument('--q_01pc_u2_window_313', type=float, help='')
        pars.add_argument('--q_01pc_u2_window_401', type=float, help='')
        pars.add_argument('--q_01pc_u2_window_402', type=float, help='')
        pars.add_argument('--q_01pc_u2_window_403', type=float, help='')
        pars.add_argument('--q_01pc_u2_window_411', type=float, help='')
        pars.add_argument('--q_01pc_u2_window_412', type=float, help='')
        pars.add_argument('--q_01pc_u2_window_413', type=float, help='')
        pars.add_argument('--q_01pc_u2_window_501', type=float, help='')
        pars.add_argument('--q_01pc_u2_window_502', type=float, help='')
        pars.add_argument('--q_01pc_u2_window_503', type=float, help='')
        pars.add_argument('--q_01pc_u2_window_511', type=float, help='')
        pars.add_argument('--q_01pc_u2_window_512', type=float, help='')
        pars.add_argument('--q_01pc_u2_window_513', type=float, help='')

        pars.add_argument('--q_01pc_u2_insert_001', type=float, help='L')
        pars.add_argument('--q_01pc_u2_insert_002', type=float, help='W')
        pars.add_argument('--q_01pc_u2_insert_003', type=float, help='H')
        pars.add_argument('--q_01pc_u2_insert_011', type=float, help='Aper')
        pars.add_argument('--q_01pc_u2_insert_012', type=float, help='Anch')
        pars.add_argument('--q_01pc_u2_insert_013', type=float, help='Groo')
        pars.add_argument('--q_01pc_u2_insert_101', type=float, help='')
        pars.add_argument('--q_01pc_u2_insert_102', type=float, help='')
        pars.add_argument('--q_01pc_u2_insert_103', type=float, help='')
        pars.add_argument('--q_01pc_u2_insert_111', type=float, help='')
        pars.add_argument('--q_01pc_u2_insert_112', type=float, help='')
        pars.add_argument('--q_01pc_u2_insert_113', type=float, help='')
        pars.add_argument('--q_01pc_u2_insert_201', type=float, help='')
        pars.add_argument('--q_01pc_u2_insert_202', type=float, help='')
        pars.add_argument('--q_01pc_u2_insert_203', type=float, help='')
        pars.add_argument('--q_01pc_u2_insert_211', type=float, help='')
        pars.add_argument('--q_01pc_u2_insert_212', type=float, help='')
        pars.add_argument('--q_01pc_u2_insert_213', type=float, help='')
        pars.add_argument('--q_01pc_u2_insert_301', type=float, help='')
        pars.add_argument('--q_01pc_u2_insert_302', type=float, help='')
        pars.add_argument('--q_01pc_u2_insert_303', type=float, help='')
        pars.add_argument('--q_01pc_u2_insert_311', type=float, help='')
        pars.add_argument('--q_01pc_u2_insert_312', type=float, help='')
        pars.add_argument('--q_01pc_u2_insert_313', type=float, help='')

# design #2: hard boxshell
        pars.add_argument('--z_02pc_c', type=str, help='') # hard
        pars.add_argument('--z_02pc_g', type=str, help='')

        pars.add_argument('--q_02pc_u1_enable', type=bool, help='')
        pars.add_argument('--q_02pc_u2_enable', type=bool, help='')
        
        pars.add_argument('--q_02pc_u1_00L', type=float, help='L')
        pars.add_argument('--q_02pc_u1_00W', type=float, help='W')
        pars.add_argument('--q_02pc_u1_00H', type=float, help='H')
        pars.add_argument('--q_02pc_u2_00L', type=float, help='L')
        pars.add_argument('--q_02pc_u2_00W', type=float, help='W')
        pars.add_argument('--q_02pc_u2_00H', type=float, help='H')

# design #3: standalone insert
        pars.add_argument('--z_03in_g', type=str, help='') # insert

        pars.add_argument('--q_03in_00L', type=float, help='Leng')
        pars.add_argument('--q_03in_00W', type=float, help='Widt')
        pars.add_argument('--q_03in_00H', type=float, help='Heig')
        pars.add_argument('--q_03in_0E1', type=float, help='dep1')
        pars.add_argument('--q_03in_0E2', type=float, help='dep2')
        pars.add_argument('--q_03in_0E3', type=float, help='dep3')
        pars.add_argument('--q_03in_011', type=float, help='In.X')
        pars.add_argument('--q_03in_012', type=float, help='In.Y')
        pars.add_argument('--q_03in_013', type=float, help='In.C')
        pars.add_argument('--q_03in_0F1', type=float, help='Ou.X')
        pars.add_argument('--q_03in_0F2', type=float, help='Ou.Y')
        pars.add_argument('--q_03in_0F3', type=float, help='Ou.C')
        pars.add_argument('--q_03in_0F4', type=float, help='Ou.A')

        pars.add_argument('--q_03in_10L', type=float, help='Leng')
        pars.add_argument('--q_03in_10W', type=float, help='Widt')
        pars.add_argument('--q_03in_10H', type=float, help='Heig')
        pars.add_argument('--q_03in_1E1', type=float, help='dep1')
        pars.add_argument('--q_03in_1E2', type=float, help='dep2')
        pars.add_argument('--q_03in_1E3', type=float, help='dep3')
        pars.add_argument('--q_03in_111', type=float, help='In.X')
        pars.add_argument('--q_03in_112', type=float, help='In.Y')
        pars.add_argument('--q_03in_113', type=float, help='In.C')
        pars.add_argument('--q_03in_1F1', type=float, help='Ou.X')
        pars.add_argument('--q_03in_1F2', type=float, help='Ou.Y')
        pars.add_argument('--q_03in_1F3', type=float, help='Ou.C')
        pars.add_argument('--q_03in_1F4', type=float, help='Ou.A')

        pars.add_argument('--q_03in_20L', type=float, help='Leng')
        pars.add_argument('--q_03in_20W', type=float, help='Widt')
        pars.add_argument('--q_03in_20H', type=float, help='Heig')
        pars.add_argument('--q_03in_2E1', type=float, help='dep1')
        pars.add_argument('--q_03in_2E2', type=float, help='dep2')
        pars.add_argument('--q_03in_2E3', type=float, help='dep3')
        pars.add_argument('--q_03in_211', type=float, help='In.X')
        pars.add_argument('--q_03in_212', type=float, help='In.Y')
        pars.add_argument('--q_03in_213', type=float, help='In.C')
        pars.add_argument('--q_03in_2F1', type=float, help='Ou.X')
        pars.add_argument('--q_03in_2F2', type=float, help='Ou.Y')
        pars.add_argument('--q_03in_2F3', type=float, help='Ou.C')
        pars.add_argument('--q_03in_2F4', type=float, help='Ou.A')

        pars.add_argument('--q_03in_30L', type=float, help='Leng')
        pars.add_argument('--q_03in_30W', type=float, help='Widt')
        pars.add_argument('--q_03in_30H', type=float, help='Heig')
        pars.add_argument('--q_03in_3E1', type=float, help='dep1')
        pars.add_argument('--q_03in_3E2', type=float, help='dep2')
        pars.add_argument('--q_03in_3E3', type=float, help='dep3')
        pars.add_argument('--q_03in_311', type=float, help='In.X')
        pars.add_argument('--q_03in_312', type=float, help='In.Y')
        pars.add_argument('--q_03in_313', type=float, help='In.C')
        pars.add_argument('--q_03in_3F1', type=float, help='Ou.X')
        pars.add_argument('--q_03in_3F2', type=float, help='Ou.Y')
        pars.add_argument('--q_03in_3F3', type=float, help='Ou.C')
        pars.add_argument('--q_03in_3F4', type=float, help='Ou.A')

        pars.add_argument('--q_03in_40L', type=float, help='Leng')
        pars.add_argument('--q_03in_40W', type=float, help='Widt')
        pars.add_argument('--q_03in_40H', type=float, help='Heig')
        pars.add_argument('--q_03in_4E1', type=float, help='dep1')
        pars.add_argument('--q_03in_4E2', type=float, help='dep2')
        pars.add_argument('--q_03in_4E3', type=float, help='dep3')
        pars.add_argument('--q_03in_411', type=float, help='In.X')
        pars.add_argument('--q_03in_412', type=float, help='In.Y')
        pars.add_argument('--q_03in_413', type=float, help='In.C')
        pars.add_argument('--q_03in_4F1', type=float, help='Ou.X')
        pars.add_argument('--q_03in_4F2', type=float, help='Ou.Y')
        pars.add_argument('--q_03in_4F3', type=float, help='Ou.C')
        pars.add_argument('--q_03in_4F4', type=float, help='Ou.A')

        pars.add_argument('--q_03in_50L', type=float, help='Leng')
        pars.add_argument('--q_03in_50W', type=float, help='Widt')
        pars.add_argument('--q_03in_50H', type=float, help='Heig')
        pars.add_argument('--q_03in_5E1', type=float, help='dep1')
        pars.add_argument('--q_03in_5E2', type=float, help='dep2')
        pars.add_argument('--q_03in_5E3', type=float, help='dep3')
        pars.add_argument('--q_03in_511', type=float, help='In.X')
        pars.add_argument('--q_03in_512', type=float, help='In.Y')
        pars.add_argument('--q_03in_513', type=float, help='In.C')
        pars.add_argument('--q_03in_5F1', type=float, help='Ou.X')
        pars.add_argument('--q_03in_5F2', type=float, help='Ou.Y')
        pars.add_argument('--q_03in_5F3', type=float, help='Ou.C')
        pars.add_argument('--q_03in_5F4', type=float, help='Ou.A')

# design 4: imposition / collage
        pars.add_argument('--q_04im_01_type', type=int, help='')
        pars.add_argument('--q_04im_01_bind', type=int, help='')
        pars.add_argument('--q_04im_01_XX', type=int, help='')
        pars.add_argument('--q_04im_01_YY', type=int, help='')
        pars.add_argument('--q_04im_02_type', type=int, help='')
        pars.add_argument('--q_04im_02_bind', type=int, help='')
        pars.add_argument('--q_04im_02_XX', type=int, help='')
        pars.add_argument('--q_04im_02_YY', type=int, help='')
        pars.add_argument('--q_04im_03_type', type=int, help='')
        pars.add_argument('--q_04im_03_bind', type=int, help='')
        pars.add_argument('--q_04im_03_XX', type=int, help='')
        pars.add_argument('--q_04im_03_YY', type=int, help='')
        pars.add_argument('--q_04im_04_type', type=int, help='')
        pars.add_argument('--q_04im_04_bind', type=int, help='')
        pars.add_argument('--q_04im_04_XX', type=int, help='')
        pars.add_argument('--q_04im_04_YY', type=int, help='')

        pars.add_argument('--q_04im_00_layout', type=int, help='')
        pars.add_argument('--q_04im_00_target', type=int, help='')

# design 5: regular slotted shipping container
        pars.add_argument('--z_05ou_g', type=str, help='') # outset

        pars.add_argument('--q_05ou_01_type', type=int, help='')
        pars.add_argument('--q_05ou_01_bind', type=int, help='')
        pars.add_argument('--q_05ou_01_unit', type=int, help='')
        pars.add_argument('--q_05ou_01_height', type=int, help='')
        pars.add_argument('--q_05ou_01_quantity', type=int, help='')
        pars.add_argument('--q_05ou_01_len', type=int, help='')
        pars.add_argument('--q_05ou_01_wid', type=int, help='')

        pars.add_argument('--q_05ou_02_type', type=int, help='')
        pars.add_argument('--q_05ou_02_bind', type=int, help='')
        pars.add_argument('--q_05ou_02_unit', type=int, help='')
        pars.add_argument('--q_05ou_02_height', type=int, help='')
        pars.add_argument('--q_05ou_02_quantity', type=int, help='')
        pars.add_argument('--q_05ou_02_len', type=int, help='')
        pars.add_argument('--q_05ou_02_wid', type=int, help='')

# design 6: palletisation plan
        pars.add_argument('--q_06pa_01_z1', type=str, help='')
        pars.add_argument('--q_06pa_01_z2', type=str, help='')
        pars.add_argument('--q_06pa_02_z1', type=str, help='')
        pars.add_argument('--q_06pa_02_z2', type=str, help='')



    def get_arguments(__):
        # Standard inkscape options input; returns a namespace.
        __._option_ = __.options
        # Dictionaries are a more useful structure for looping purposes than namespaces.
        __._ = __._option_.__dict__
	
        # Now; before we attempt anything else...
        __.debug=[
          __._['debug0'], # Output plot categorisation and raw tracing data
          __._['debug1'], # Supplimental database
          __._['debug2'], # Supplimental tablesheet and document
          __._['debug3'], # Supplimental drawing and presentation
        ]
        
        ## 00, All settings
        __.z0all0= {
          'absolute': __._['q_0all_measure_absolute'],
          'relative': __._['q_0all_measure_relative'],
        }
        ## Includes:
        ##   measurement unit, & scale unit
        
        ## 01, Job settings
        __.z0job0= {
          # Our Company/Server's job number and Client's catalogue number
          'dognum': __._['q_00dognum_01user'],
          'catnum': __._['q_00catnum_02user'],
          # Sheet composition and caliper in micrometers
          'material': __._['q_0all_medium_type'],
          'mcaliper': __._['q_0all_medium_cali'],
          # draw a half or full cube or expose the grid; all for diagnostics.
          'fullcube': __._['q_0all_area_amount'],
          'griddraw': __._['q_0all_grid_type'],
          # page size
          'page': [ __._['q_0all_medium_x'], __._['q_0all_medium_y'] ],
          # plotting offset, next component offset
          'offset':[
            [ __._['q_0all_origin_x'], __._['q_0all_origin_y'] ],
            [ __._['q_0all_offset_x'], __._['q_0all_offset_y'] ],],
        }
        ## Includes:

        ## media type
        ## drawing diagnostic
        #__.z0q0optional={
        #}
        
	##
	## 01, carton
        __.z1carton={
          'Quantity': 2, # Not to be used; we will count the number of elements in the array.
          'Enable': [ __._['q_01pc_u1_enable'], __._['q_01pc_u2_enable'], ],
          'FlapHeight': [ [], [] ],
          'GRID':[ [],[], ],
          'GridWindow':[ [],[], ],
          'GridInsert':[ [],[], ],
          'PLAN':[ [],[], ],
          'PlanWindow':[ [],[] ],
          'PlanInsert':[ [],[] ],
          'Leng':[__._['q_01pc_u1_00L'],__._['q_01pc_u2_00L'],],
          'Widt':[__._['q_01pc_u1_00W'],__._['q_01pc_u2_00W'],],
          'Heig':[__._['q_01pc_u1_00H'],__._['q_01pc_u2_00H'],],
          'Lidd':[__._['q_01pc_u1_00_lidd'],__._['q_01pc_u2_00_lidd'],],
          'Base':[__._['q_01pc_u1_00_base'],__._['q_01pc_u2_00_base'],],
          'Hang':[__._['q_01pc_u1_00_hang'],__._['q_01pc_u2_00_hang'],],
          'Flap':[__._['q_01pc_u1_00_flap'],__._['q_01pc_u2_00_flap'],],
          'LiddOrient':[__._['q_01pc_u1_00_lidd_o'],__._['q_01pc_u2_00_lidd_o'],],
          'BaseOrient':[__._['q_01pc_u1_00_base_o'],__._['q_01pc_u2_00_base_o'],],
          'Window':
          [
           {# 0-5=position; 0=size,1=offset; 1-3=unit
            'Xi':[
            __._['q_01pc_u1_window_001'],__._['q_01pc_u1_window_101'],__._['q_01pc_u1_window_201'],
            __._['q_01pc_u1_window_301'],__._['q_01pc_u1_window_401'],__._['q_01pc_u1_window_501']],
            'Yi':[
            __._['q_01pc_u1_window_002'],__._['q_01pc_u1_window_102'],__._['q_01pc_u1_window_202'],
            __._['q_01pc_u1_window_302'],__._['q_01pc_u1_window_402'],__._['q_01pc_u1_window_502']],
            'Curved':[
            __._['q_01pc_u1_window_003'],__._['q_01pc_u1_window_103'],__._['q_01pc_u1_window_203'],
            __._['q_01pc_u1_window_303'],__._['q_01pc_u1_window_403'],__._['q_01pc_u1_window_503']],
            'Xo':[
            __._['q_01pc_u1_window_011'],__._['q_01pc_u1_window_111'],__._['q_01pc_u1_window_211'],
            __._['q_01pc_u1_window_311'],__._['q_01pc_u1_window_411'],__._['q_01pc_u1_window_511']],
            'Yo':[
            __._['q_01pc_u1_window_012'],__._['q_01pc_u1_window_112'],__._['q_01pc_u1_window_212'],
            __._['q_01pc_u1_window_312'],__._['q_01pc_u1_window_412'],__._['q_01pc_u1_window_512']],
            'Anchor':[
            __._['q_01pc_u1_window_013'],__._['q_01pc_u1_window_113'],__._['q_01pc_u1_window_213'],
            __._['q_01pc_u1_window_313'],__._['q_01pc_u1_window_413'],__._['q_01pc_u1_window_513']],
           },{# 0-5=position; 0=size,1=offset; 1-3=unit
            'Xi':[
            __._['q_01pc_u2_window_001'],__._['q_01pc_u2_window_101'],__._['q_01pc_u2_window_201'],
            __._['q_01pc_u2_window_301'],__._['q_01pc_u2_window_401'],__._['q_01pc_u2_window_501']],
            'Yi':[
            __._['q_01pc_u2_window_002'],__._['q_01pc_u2_window_102'],__._['q_01pc_u2_window_202'],
            __._['q_01pc_u2_window_302'],__._['q_01pc_u2_window_402'],__._['q_01pc_u2_window_502']],
            'Curved':[
            __._['q_01pc_u2_window_003'],__._['q_01pc_u2_window_103'],__._['q_01pc_u2_window_203'],
            __._['q_01pc_u2_window_303'],__._['q_01pc_u2_window_403'],__._['q_01pc_u2_window_503']],
            'Xo':[
            __._['q_01pc_u2_window_011'],__._['q_01pc_u2_window_111'],__._['q_01pc_u2_window_211'],
            __._['q_01pc_u2_window_311'],__._['q_01pc_u2_window_411'],__._['q_01pc_u2_window_511']],
            'Yo':[
            __._['q_01pc_u2_window_012'],__._['q_01pc_u2_window_112'],__._['q_01pc_u2_window_212'],
            __._['q_01pc_u2_window_312'],__._['q_01pc_u2_window_412'],__._['q_01pc_u2_window_512']],
            'Anchor':[
            __._['q_01pc_u2_window_013'],__._['q_01pc_u2_window_113'],__._['q_01pc_u2_window_213'],
            __._['q_01pc_u2_window_313'],__._['q_01pc_u2_window_413'],__._['q_01pc_u2_window_513']],
           }
          ],
          'Insert':
          [
           {
            'Li':[
            __._['q_01pc_u1_insert_001'],__._['q_01pc_u1_insert_101'],__._['q_01pc_u1_insert_201'],
            __._['q_01pc_u1_insert_301'],],
            #__._['q_01pc_u1_insert_401'],__._['q_01pc_u1_insert_501'],],
            'Wi':[
            __._['q_01pc_u1_insert_002'],__._['q_01pc_u1_insert_102'],__._['q_01pc_u1_insert_202'],
            __._['q_01pc_u1_insert_302'],],
            #__._['q_01pc_u1_insert_402'],__._['q_01pc_u1_insert_502'],],
            'Hi':[
            __._['q_01pc_u1_insert_003'],__._['q_01pc_u1_insert_103'],__._['q_01pc_u1_insert_203'],
            __._['q_01pc_u1_insert_303'],],
            #__._['q_01pc_u1_insert_403'],__._['q_01pc_u1_insert_503'],],
            'Ba':[
            __._['q_01pc_u1_insert_011'],__._['q_01pc_u1_insert_111'],__._['q_01pc_u1_insert_211'],
            __._['q_01pc_u1_insert_311'],],
            #__._['q_01pc_u1_insert_411'],__._['q_01pc_u1_insert_511'],],
            'Di':[
            __._['q_01pc_u1_insert_012'],__._['q_01pc_u1_insert_112'],__._['q_01pc_u1_insert_212'],
            __._['q_01pc_u1_insert_312'],],
            #__._['q_01pc_u1_insert_412'],__._['q_01pc_u1_insert_512'],],
            'Gr':[
            __._['q_01pc_u1_insert_013'],__._['q_01pc_u1_insert_113'],__._['q_01pc_u1_insert_213'],
            __._['q_01pc_u1_insert_313'],],
            #__._['q_01pc_u1_insert_413'],__._['q_01pc_u1_insert_513'],],
           },{
            'Li':[
            __._['q_01pc_u2_insert_001'],__._['q_01pc_u2_insert_101'],__._['q_01pc_u2_insert_201'],
            __._['q_01pc_u2_insert_301'],],
            #__._['q_01pc_u2_insert_401'],__._['q_01pc_u2_insert_501'],],
            'Wi':[
            __._['q_01pc_u2_insert_002'],__._['q_01pc_u2_insert_102'],__._['q_01pc_u2_insert_202'],
            __._['q_01pc_u2_insert_302'],],
            #__._['q_01pc_u2_insert_402'],__._['q_01pc_u2_insert_502'],],
            'Hi':[
            __._['q_01pc_u2_insert_003'],__._['q_01pc_u2_insert_103'],__._['q_01pc_u2_insert_203'],
            __._['q_01pc_u2_insert_303'],],
            #__._['q_01pc_u2_insert_403'],__._['q_01pc_u2_insert_503'],],
            'Ba':[
            __._['q_01pc_u2_insert_011'],__._['q_01pc_u2_insert_111'],__._['q_01pc_u2_insert_211'],
            __._['q_01pc_u2_insert_311'],],
            #__._['q_01pc_u2_insert_411'],__._['q_01pc_u2_insert_511'],],
            'Di':[
            __._['q_01pc_u2_insert_012'],__._['q_01pc_u2_insert_112'],__._['q_01pc_u2_insert_212'],
            __._['q_01pc_u2_insert_312'],],
            #__._['q_01pc_u2_insert_412'],__._['q_01pc_u2_insert_512'],],
            'Gr':[
            __._['q_01pc_u2_insert_013'],__._['q_01pc_u2_insert_113'],__._['q_01pc_u2_insert_213'],
            __._['q_01pc_u2_insert_313'],],
            #__._['q_01pc_u2_insert_413'],__._['q_01pc_u2_insert_513'],],
           }
          ],
        }

        ##
        ## 02, rigidbox
        __.z2rigbox={
          'Quantity': 2, # if this is used, it will be the number of conjoined impressions up.
          'Enable': [ __._['q_02pc_u1_enable'], __._['q_02pc_u2_enable'], ],
          'GRID':[ [],[], ],
          'PLAN':[ [],[], ], #ya
          'Leng':[__._['q_02pc_u1_00L'],__._['q_02pc_u2_00L'],],
          'Widt':[__._['q_02pc_u1_00W'],__._['q_02pc_u2_00W'],],
          'Heig':[__._['q_02pc_u1_00H'],__._['q_02pc_u2_00H'],],
        }
        
        ## 03, lone insert
        ##
        __.z3insert={
          'GRID':[],
          'PLAN':[], #ya
          'Li':[
          __._['q_03in_00L'],__._['q_03in_10L'],__._['q_03in_20L'],
          __._['q_03in_30L'],__._['q_03in_40L'],__._['q_03in_50L'],],
          'Wi':[
          __._['q_03in_00W'],__._['q_03in_10W'],__._['q_03in_20W'],
          __._['q_03in_30W'],__._['q_03in_40W'],__._['q_03in_50W'],],
          'Hi':[
          __._['q_03in_00H'],__._['q_03in_10H'],__._['q_03in_20H'],
          __._['q_03in_30H'],__._['q_03in_40H'],__._['q_03in_50H'],],
          'Ba':[
          __._['q_03in_011'],__._['q_03in_111'],__._['q_03in_211'],
          __._['q_03in_311'],__._['q_03in_411'],__._['q_03in_511'],],
          'Di':[
          __._['q_03in_012'],__._['q_03in_112'],__._['q_03in_212'],
          __._['q_03in_312'],__._['q_03in_412'],__._['q_03in_512'],],
          'Gr':[
          __._['q_03in_013'],__._['q_03in_113'],__._['q_03in_213'],
          __._['q_03in_313'],__._['q_03in_413'],__._['q_03in_513'],],
        }

        ##
        ## 04, imposition
        __.z4impose={
          'GRID':[],
          'PLAN':[], #ya
        }

        ##
        ## 05, taped box
        __.z5outset={
          'GRID':[],
          'PLAN':[], #ya
          'FlapHeight': [ [], [] ],
          'Type':[ __._['q_05ou_01_type'], __._['q_05ou_01_type'] ],
          'Bind':[ __._['q_05ou_01_bind'], __._['q_05ou_02_bind'] ],
          'Height':[
            __._['q_05ou_01_height'], __._['q_05ou_02_height']
          ],
          'Quantity':[
            __._['q_05ou_01_quantity'], __._['q_05ou_02_quantity']
          ],
          'Len':[
            __._['q_05ou_01_len'], __._['q_05ou_02_len']
          ],
          'Wid':[
            __._['q_05ou_01_wid'], __._['q_05ou_02_wid']
          ],
        }

        ##
        ## 06, palletisation
        __.z6pallet={
          'GRID':[],
          'PLAN':[], #ya
        }

        ##
        ## StyleSheet
        __._stylesheet_={
        # fold style
        'q_fold_base': { # the four fixed sides
          'stroke'        : __._['q_col1_cre5'], #'#00FFFF', # Cyan Crease
          'stroke-width'  : __._['q_col1_cre2'], # thick crease line
          'stroke-opacity': __._['q_col1_cre3'], # very legible but not obstructing background
          'fill'          : 'none'
        },
        'q_fold_glue_tab': { # the one glue tab
          'stroke'        : __._['q_col1_cre4'], #'#406080', # Cyan Crease
          'stroke-width'  : __._['q_col1_cre2'], # thick crease line
          'stroke-opacity': __._['q_col1_cre3'], # very legible but not obstructing background
          'fill'          : 'none'
        },
        'q_fold_hinge': { # the two moving lid hinges
          'stroke'        : __._['q_col1_cre6'], #'#00FFC0', # Cyan Crease
          'stroke-width'  : __._['q_col1_cre2'], # thick crease line
          'stroke-opacity': __._['q_col1_cre3'], # legible but distinct from base/permanent fold
          'fill'          : 'none'
        },
        'q_fold_lid_tab': { # the opposite ends of two lid hinges
          'stroke'        : __._['q_col1_cre7'], #'#00C0E0', # Cyan Crease
          'stroke-width'  : __._['q_col1_cre2'], # thick crease line
          'stroke-opacity': __._['q_col1_cre3'], # legible but distinct from base/permanent fold
          'fill'          : 'none'
        },
        # Window fold (for 1-piece substitue for an insert)
        'q_fold_window': { # the opposite ends of two lid hinges
          'stroke'        : __._['q_col1_cre9'], #'#00C0E0', # Cyan Crease
          'stroke-width'  : __._['q_col1_cre2'], # thick crease line
          'stroke-opacity': __._['q_col1_cre3'], # legible but distinct from base/permanent fold
          'fill'          : 'none'
        },
        # Insert fold
        'q_fold_insert': { # the opposite ends of two lid hinges
          'stroke'        : __._['q_col1_creA'], #'#00C0E0', # Cyan Crease
          'stroke-width'  : __._['q_col1_cre2'], # thick crease line
          'stroke-opacity': __._['q_col1_cre3'], # legible but distinct from base/permanent fold
          'fill'          : 'none'
        },
        # Regular Slotted Shipping Container fold
        'q_fold_outset': { # the opposite ends of two lid hinges
          'stroke'        : __._['q_col1_cre1'], #'#00C0E0', # Cyan Crease
          'stroke-width'  : __._['q_col1_cre2'], # thick crease line
          'stroke-opacity': __._['q_col1_cre3'], # legible but distinct from base/permanent fold
          'fill'          : 'none'
        },
        # chop style
        'q_chop_out': { # cut outside, closed or open paths
          'stroke'        : __._['q_col1_cut4'], #'#FF00FF', # Magenta Cut
          'stroke-width'  : __._['q_col1_cut2'], # thin cut line
          'stroke-opacity': __._['q_col1_cut3'], # very legible but not obstructing background
          'fill'          : 'none', #'#002000', # Use only to determine shape area.
          'fill-opacity'  : 0.2 # Diagnostic fill feature is 20% opaque.
        },
        'q_chop_inn': { # cut inside, open paths
          'stroke'        : __._['q_col1_cut8'], #'#FFC0FF', # Magenta Cut
          'stroke-width'  : __._['q_col1_cut2'], # thin cut line
          'stroke-opacity': __._['q_col1_cut3'], # very legible but not obstructing background
          'fill'          : 'none', # Use only to determine shape area.
          'fill-opacity'  : 0.2 # Diagnostic fill features are 80% opaque.
        },
        # Window Chops
        'q_chop_out_window': { # window breaks out of the edges of the carton (hypothetical)
          'stroke'        : __._['q_col1_cutC'], #'#FFC0FF', # Magenta Cut
          'stroke-width'  : __._['q_col1_cut2'], # thin cut line
          'stroke-opacity': __._['q_col1_cut3'], # Bring windows to an obvious light.
          'fill'          : 'none', # Use only to determine shape area.
          'fill-opacity'  : 0.2 # Diagnostic fill features are 80% opaque.
        },
        'q_chop_inn_window': { # window contained within carton
          'stroke'        : __._['q_col1_cutA'], #'#FFC0FF', # Magenta Cut
          'stroke-width'  : __._['q_col1_cut2'], # thin cut line
          'stroke-opacity': __._['q_col1_cut3'], # Bring windows to an obvious light.
          'fill'          : 'none', # Use only to determine shape area.
          'fill-opacity'  : 0.2 # Diagnostic fill features are 80% opaque.
        },
        # Insert Chops
        'q_chop_out_insert': { # cut outside, closed or open paths
          'stroke'        : __._['q_col1_cutD'], #'#FF00FF', # Magenta Cut
          'stroke-width'  : __._['q_col1_cut2'], # thin cut line
          'stroke-opacity': __._['q_col1_cut3'], # very legible but not obstructing background
          'fill'          : 'none', #'#002000', # Use only to determine shape area.
          'fill-opacity'  : 0.2 # Diagnostic fill feature is 20% opaque.
        },
        'q_chop_inn_insert': { # cut inside, open paths
          'stroke'        : __._['q_col1_cutB'], #'#FFC0FF', # Magenta Cut
          'stroke-width'  : __._['q_col1_cut2'], # thin cut line
          'stroke-opacity': __._['q_col1_cut3'], # very legible but not obstructing background
          'fill'          : 'none', # Use only to determine shape area.
          'fill-opacity'  : 0.2 # Diagnostic fill features are 80% opaque.
        },
        # Regular Slotted Shipping Container Chops
        'q_chop_out_outset': { # cut outside, closed or open paths
          'stroke'        : __._['q_col1_cut1'], #'#FF00FF', # Magenta Cut
          'stroke-width'  : __._['q_col1_cut2'], # thin cut line
          'stroke-opacity': __._['q_col1_cut3'], # very legible but not obstructing background
          'fill'          : 'none', #'#002000', # Use only to determine shape area.
          'fill-opacity'  : 0.2 # Diagnostic fill feature is 20% opaque.
        },
        'q_chop_inn_outset': { # cut inside, open paths
          'stroke'        : __._['q_col1_cut1'], #'#FFC0FF', # Magenta Cut
          'stroke-width'  : __._['q_col1_cut2'], # thin cut line
          'stroke-opacity': __._['q_col1_cut3'], # very legible but not obstructing background
          'fill'          : 'none', # Use only to determine shape area.
          'fill-opacity'  : 0.2 # Diagnostic fill features are 80% opaque.
        },
        # SoftCarton Special Chops
        'q_chop_out_basewall': { # this is what to plot where there are no dust flaps or lid and base breakouts.
          'stroke'        : __._['q_col1_cut7'], #'#FF00FF', # Magenta Cut
          'stroke-width'  : __._['q_col1_cut2'], # thin cut line
          'stroke-opacity': __._['q_col1_cut3'], # less significant
          'fill'          : 'none', #'#002000', # Use only to determine shape area.
          'fill-opacity'  : 0.2 # Diagnostic fill feature is 80% translucent.
        },
        'q_chop_out_sidewall': { # left and right side walls and glue tabs
          'stroke'        : __._['q_col1_cut7'], #'#FF00FF', # Magenta Cut
          'stroke-width'  : __._['q_col1_cut2'], # thin cut line
          'stroke-opacity': __._['q_col1_cut3'], # less significant
          'fill'          : 'none', #'#002000', # Use only to determine shape area.
          'fill-opacity'  : 0.2 # Diagnostic fill feature is 80% translucent.
        },
        'q_chop_out_flap_out': { # lid and base (outer)
          'stroke'        : __._['q_col1_cut5'], #'#FF00FF', # Magenta Cut
          'stroke-width'  : __._['q_col1_cut2'], # thin cut line
          'stroke-opacity': __._['q_col1_cut3'], # dead obvious lid compensation
          'fill'          : 'none', #'#002000', # Use only to determine shape area.
          'fill-opacity'  : 0.2 # Diagnostic fill feature is 80% translucent.
        },
        'q_chop_out_flap_inn': { # dust flaps (inner)
          'stroke'        : __._['q_col1_cut6'], #'#FF00FF', # Magenta Cut
          'stroke-width'  : __._['q_col1_cut2'], # thin cut line
          'stroke-opacity': __._['q_col1_cut3'], # dead obvious flap compensation
          'fill'          : 'none', #'#002000', # Use only to determine shape area.
          'fill-opacity'  : 0.2 # Diagnostic fill feature is 80% translucent.
        },
        'q_chop_inn_tab': { # tab hitches for gripping onto dust flaps
          'stroke'        : __._['q_col1_cut9'], #'#FFC0FF', # Magenta Cut
          'stroke-width'  : __._['q_col1_cut2'], # thin cut line
          'stroke-opacity': __._['q_col1_cut3'], # Mark a discernable difference between isolated cuts and the continous contour.
          'fill'          : 'none', # Use only to determine shape area.
          'fill-opacity'  : 0.2 # Diagnostic fill features are 80% translucent.
        },
        'q_chop_inn_hang': { # tab hitches for gripping onto dust flaps
          'stroke'        : __._['q_col1_cut8'], #'#FFC0FF', # Magenta Cut
          'stroke-width'  : __._['q_col1_cut2'], # thin cut line
          'stroke-opacity': __._['q_col1_cut3'], # Mark a discernable difference between isolated cuts and the continous contour.
          'fill'          : 'none', # Use only to determine shape area.
          'fill-opacity'  : 0.2 # Diagnostic fill features are 80% translucent.
        },
        # registration style
        'q_register': { # calibration markers for combinded printing and plotting
          'stroke'        : __._['q_col1_reg1'], #'#97B723', # Registration Yellow
          'stroke-width'  : __._['q_col1_reg2'], # 1mm provides decent visibility and minimal issue centering.
          'stroke-opacity': __._['q_col1_reg3'], # registration lines need to be fairly obvious to both operator and plotter.
          'fill'          : 'none', # required for closed paths intended for a cutting plotter!
          'fill-opacity'  : 0.2 # Diagnostic feature is 20% opaque.
        },
        'q_regitype': { # registration co-ordinates to plot
          'stroke'        : 'none',
          'stroke-width'  : '0.02px',
          'stroke-opacity': __._['q_col1_reg3'],
          'font-size'     : '1.5px',
          'fill'          : '#FF8800',
          'fill-opacity'  : 0.75
        },
        'q_register_brother_1': { # calibration markers for combinded printing and plotting
          'stroke'        : '#000000', # Black
          'stroke-width'  : '1.0mm', # 
          'stroke-opacity': 1.0, # 
          'fill'          : 'none', # Oh Brother.
          'fill-opacity'  : 1.0 # 
        },
        'q_register_kongsberg_1': { # calibration markers for combinded printing and plotting
          'stroke'        : '#000000', # Black
          'stroke-width'  : '1.0mm', # 
          'stroke-opacity': 1.0, # 
          'fill'          : '#000000', # Oh Kongsberg!
          'fill-opacity'  : 1.0 # 
        },
        # diagnostic style
        'q_diagnose': { # highlight points of interest, including the major grid we bind our carton cut and crease lines to.
          'stroke'        : __._['q_col1_dia1'], #'#00FF00', # Diagnostic Green
          'stroke-width'  : __._['q_col1_dia2'], # default to 3mm, "because the troll must become obvious!"
          'stroke-opacity': __._['q_col1_reg3'], # diagnostic lines must not interfere with the viewing of the primary working subject matter.
          'fill'          : 'none', # required for closed paths intended for a cutting plotter!
          'fill-opacity'  : 0.2 # Diagnostic feature is 80% translucent.
        },
        'q_diagtype': { # diagnostic output to plot
          'stroke'        : 'none',
          'stroke-width'  : '0.05px',
          'stroke-opacity': __._['q_col1_reg3'],
          'font-size'     : '1.5px',
          'fill'          : '#FF0000',
          'fill-opacity'  : 0.75
        },
        }



def main():
    effect = aSyn3c91()
    effect.run()


if __name__ == '__main__':
    main()

