<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8" />
    <title>Ideal Spouse Age Calculator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
        }

        h1 {
            margin-bottom: 20px;
        }

        img {
            width: 300px;
            height: 200px; /* Adjust as needed */
            margin-bottom: 20px;
        }

        table {
            margin: 0 auto;
            border-collapse: collapse; /* Avoid default border spacing */
        }

        td {
            padding: 10px;
            border: 1px solid #ddd;
        }

        .error {
            color: red;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <h1>Ideal Spouse Age Calculator</h1>
    <img src="images/banner.png" alt="Ideal Spouse Age Calculator Banner" />

    <hr />

    <table>
        <tr>
            <td>Enter your age:</td>
            <td><input type="text" id="TextBoxAge" runat="server" /></td>
        </tr>
        <tr>
            <td>Choose your gender:</td>
            <td>
                <asp:Button ID="ButtonMale" runat="server" Text="I am a male" OnClick="CalculateSpouseAge" />
                <asp:Button ID="ButtonFemale" runat="server" Text="I am a female" OnClick="CalculateSpouseAge" />
            </td>
        </tr>
        <tr>
            <td colspan="2">
                <asp:Label ID="LabelResults" runat="server" Text="" />
            </td>
        </tr>
    </table>

    <script type="text/javascript">
        // Not required in this implementation
    </script>
</body>
</html>
