Public num As Integer
Sub s()
Dim i As Integer
For i = 2 To 9999
If Range("C" & i) = "" Then
num = i
Exit For
End If
 Range("AB1").Select
ActiveCell.FormulaR1C1 = "=RC[-25]"
Range("AB" & i).Select 
 ActiveCell.FormulaR1C1 = "=RC[-25]/R2C3-1"
 Range("AC1").Select
ActiveCell.FormulaR1C1 = "=RC[-25]"
Range("AC" & i).Select 
 ActiveCell.FormulaR1C1 = "=RC[-25]/R2C4-1"
 Range("AD1").Select
ActiveCell.FormulaR1C1 = "=RC[-25]"
Range("AD" & i).Select 
 ActiveCell.FormulaR1C1 = "=RC[-25]/R2C5-1"
 Range("AE1").Select
ActiveCell.FormulaR1C1 = "=RC[-25]"
Range("AE" & i).Select 
 ActiveCell.FormulaR1C1 = "=RC[-25]/R2C6-1"
 Range("AF1").Select
ActiveCell.FormulaR1C1 = "=RC[-25]"
Range("AF" & i).Select 
 ActiveCell.FormulaR1C1 = "=RC[-25]/R2C7-1"
 Range("AG1").Select
ActiveCell.FormulaR1C1 = "=RC[-25]"
Range("AG" & i).Select 
 ActiveCell.FormulaR1C1 = "=RC[-25]/R2C8-1"
 Range("AH1").Select
ActiveCell.FormulaR1C1 = "=RC[-25]"
Range("AH" & i).Select 
 ActiveCell.FormulaR1C1 = "=RC[-25]/R2C9-1"
 Range("AI1").Select
ActiveCell.FormulaR1C1 = "=RC[-25]"
Range("AI" & i).Select 
 ActiveCell.FormulaR1C1 = "=RC[-25]/R2C10-1"
 Range("AJ1").Select
ActiveCell.FormulaR1C1 = "=RC[-25]"
Range("AJ" & i).Select 
 ActiveCell.FormulaR1C1 = "=RC[-25]/R2C11-1"
 Range("AK1").Select
ActiveCell.FormulaR1C1 = "=RC[-25]"
Range("AK" & i).Select 
 ActiveCell.FormulaR1C1 = "=RC[-25]/R2C12-1"
 Range("AL1").Select
ActiveCell.FormulaR1C1 = "=RC[-25]"
Range("AL" & i).Select 
 ActiveCell.FormulaR1C1 = "=RC[-25]/R2C13-1"
 Range("AM1").Select
ActiveCell.FormulaR1C1 = "=RC[-25]"
Range("AM" & i).Select 
 ActiveCell.FormulaR1C1 = "=RC[-25]/R2C14-1"
 Range("AN1").Select
ActiveCell.FormulaR1C1 = "=RC[-25]"
Range("AN" & i).Select 
 ActiveCell.FormulaR1C1 = "=RC[-25]/R2C15-1"
 Range("AO1").Select
ActiveCell.FormulaR1C1 = "=RC[-25]"
Range("AO" & i).Select 
 ActiveCell.FormulaR1C1 = "=RC[-25]/R2C16-1"
 Range("AP1").Select
ActiveCell.FormulaR1C1 = "=RC[-25]"
Range("AP" & i).Select 
 ActiveCell.FormulaR1C1 = "=RC[-25]/R2C17-1"
 Range("AQ1").Select
ActiveCell.FormulaR1C1 = "=RC[-25]"
Range("AQ" & i).Select 
 ActiveCell.FormulaR1C1 = "=RC[-25]/R2C18-1"
 Range("AR1").Select
ActiveCell.FormulaR1C1 = "=RC[-25]"
Range("AR" & i).Select 
 ActiveCell.FormulaR1C1 = "=RC[-25]/R2C19-1"
 Range("AS1").Select
ActiveCell.FormulaR1C1 = "=RC[-25]"
Range("AS" & i).Select 
 ActiveCell.FormulaR1C1 = "=RC[-25]/R2C20-1"
 Range("AT1").Select
ActiveCell.FormulaR1C1 = "=RC[-25]"
Range("AT" & i).Select 
 ActiveCell.FormulaR1C1 = "=RC[-25]/R2C21-1"
 Range("AU1").Select
ActiveCell.FormulaR1C1 = "=RC[-25]"
Range("AU" & i).Select 
 ActiveCell.FormulaR1C1 = "=RC[-25]/R2C22-1"
 Range("AV1").Select
ActiveCell.FormulaR1C1 = "=RC[-25]"
Range("AV" & i).Select 
 ActiveCell.FormulaR1C1 = "=RC[-25]/R2C23-1"
 Range("AW1").Select
ActiveCell.FormulaR1C1 = "=RC[-25]"
Range("AW" & i).Select 
 ActiveCell.FormulaR1C1 = "=RC[-25]/R2C24-1"
 Range("AX1").Select
ActiveCell.FormulaR1C1 = "=RC[-25]"
Range("AX" & i).Select 
 ActiveCell.FormulaR1C1 = "=RC[-25]/R2C25-1"
Next
Range("AB1:AX" & num).Select
ActiveSheet.Shapes.AddChart2(227, xlLine).Select
ActiveChart.SetSourceData Source:=Range("Sheet1!$AB$1:$AX$" & num)
End Sub
