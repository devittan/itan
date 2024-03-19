using System;

public partial class _Default : System.Web.UI.Page
{
    protected void CalculateSpouseAge(object sender, EventArgs e)
    {
        try
        {
            int yourAge = int.Parse(TextBoxAge.Text);

            bool isMale = sender == ButtonMale;

            int spouseAge;

            if (isMale)
            {
                spouseAge = yourAge * 2 - 14;
            }
            else
            {
                spouseAge = yourAge / 2 + 7;
            }

            LabelResults.Text = $"The ideal age of your {(isMale ? "wife" : "husband")} is {spouseAge}.";
        }
        catch (FormatException)
        {
            LabelResults.Text = "Please enter a valid number for your age.";
            LabelResults.CssClass = "error"; // Apply error styling
        }
    }
}
