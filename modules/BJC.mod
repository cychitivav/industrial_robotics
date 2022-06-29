MODULE BJC
    CONST robtarget Home:=[[506.292,0,679.5],[0.5,0,0.866025404,0],[0,-1,0,1],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    
!    Brayan points
    CONST robtarget P1:=[[35,135,0],[0,0.707106781,0.707106781,0],[0,-1,0,1],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget P2:=[[35,85,0],[0,0.707106781,0.707106781,0],[0,-1,0,1],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget P3:=[[35,25,0],[0,0.707106781,0.707106781,0],[0,-1,0,1],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget P4:=[[60,25,0],[0,0.707106781,0.707106781,0],[0,-1,0,1],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget P5:=[[55,85,0],[0,0.707106781,0.707106781,0],[0,-1,0,1],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget P6:=[[75,115,0],[0,0.707106781,0.707106781,0],[0,-1,0,1],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget P7:=[[85,60,0],[0,0.707106781,0.707106781,0],[0,-1,0,1],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    
    CONST robtarget P7u:=[[85,60,30],[0,0.707106781,0.707106781,0],[0,-1,0,1],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]]; 
    
!    Julian points
    CONST robtarget P8:=[[100,135,0],[0,0.707106781,0.707106781,0],[0,-1,0,1],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget P9:=[[145,135,0],[0,0.707106781,0.707106781,0],[0,-1,0,1],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget P10:=[[145,50,0],[0,0.707106781,0.707106781,0],[0,-1,0,1],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget P11:=[[125,25,0],[0,0.707106781,0.707106781,0],[0,-1,0,1],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget P12:=[[100,50,0],[0,0.707106781,0.707106781,0],[0,-1,0,1],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    
    CONST robtarget P12u:=[[100,50,30],[0,0.707106781,0.707106781,0],[0,-1,0,1],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    
!    Cristian points
    CONST robtarget P13:=[[220,110,0],[0,0.707106781,0.707106781,0],[0,-1,0,1],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget P14:=[[225,125,0],[0,0.707106781,0.707106781,0],[0,-1,0,1],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget P15:=[[210,133,0],[0,0.707106781,0.707106781,0],[0,-1,0,1],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget P16:=[[180,120,0],[0,0.707106781,0.707106781,0],[0,-1,0,1],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget P17:=[[162,40,0],[0,0.707106781,0.707106781,0],[0,-1,0,1],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget P18:=[[190,25,0],[0,0.707106781,0.707106781,0],[0,-1,0,1],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget P19:=[[210,50,0],[0,0.707106781,0.707106781,0],[0,-1,0,1],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
!***********************************************************
    !
    ! Module:  write BJC
    !
    ! Description:
    !   <Insert description here>
    !
    ! Author: Cristian Chitiva, Brayan Estupinan
    !
    ! Version: 1.0
    !
    !***********************************************************
    
    
    !***********************************************************
    !
    ! Procedure main
    !
    !   This is the entry point of your program
    !
    !***********************************************************
    PROC main()
        MoveJ Home,v1000,z100,tool0;
        
        Brayan;
        MoveL P7u,v1000,z0,TipBJC\WObj:=whiteBoard;
       
        Julian;
        MoveL P12u,v1000,z0,TipBJC\WObj:=whiteBoard;
        
        Cristian;
        MoveJ Home,v1000,z0,tool0;
    ENDPROC
    PROC Brayan()
        MoveJ P5,v1000,z0,TipBJC\WObj:=whiteBoard;
        MoveL P2,v100,z0,TipBJC\WObj:=whiteBoard;
        MoveL P1,v100,z0,TipBJC\WObj:=whiteBoard;
        MoveC P6,P5,v100,z0,TipBJC\WObj:=whiteBoard;
        MoveC P7,P4,v100,z0,TipBJC\WObj:=whiteBoard;
        MoveL P3,v100,z0,TipBJC\WObj:=whiteBoard;
        MoveL P2,v100,z0,TipBJC\WObj:=whiteBoard;
    ENDPROC
    
     PROC Julian()
        MoveJ P8,v1000,z0,TipBJC\WObj:=whiteBoard;
        MoveL P9,v100,z0,TipBJC\WObj:=whiteBoard;
        MoveL P10,v100,z0,TipBJC\WObj:=whiteBoard;
        MoveC P11,P12,v100,z0,TipBJC\WObj:=whiteBoard;
    ENDPROC
    
    PROC Cristian()
        MoveJ P13,v1000,z0,TipBJC\WObj:=whiteBoard;
        MoveC P14,P15,v100,z0,TipBJC\WObj:=whiteBoard;
        MoveC P16,P17,v100,z0,TipBJC\WObj:=whiteBoard;
        MoveC P18,P19,v100,z0,TipBJC\WObj:=whiteBoard;
    ENDPROC
ENDMODULE