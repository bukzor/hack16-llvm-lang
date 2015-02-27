; ModuleID = ""
target triple = ""
target datalayout = ""


@".str4" =   global [13 x i8] c"hello\2c\20world\21"
declare i32 @"puts"(i8* %".1") 

define i32 @"main"() 
{
.1:
  %".2" = call i32 (i8*)* @"puts"(i8* getelementptr ([13 x i8]* @".str4", i32 0, i32 0))
  ret i32 0
}




