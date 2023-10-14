document.addEventListener("DOMContentLoaded", async function () {
  const connectButton = document.querySelector(".contact-button");
  const verifyButton = document.querySelector(".verify-button");

  connectButton.addEventListener("click", async () => {
    try {
      if (window.ethereum) {
        await window.ethereum.enable();
        const web3 = new Web3(window.ethereum);
        const accounts = await web3.eth.getAccounts();
        if (accounts.length > 0) {
          redirectToQuestionPage();
          console.log("Connected to Metamask.");
        } else {
          console.log("Metamask is installed, but no account is connected.");
        }
      } else {
        console.error("Metamask not detected.");
      }
    } catch (error) {
      console.error("Metamask connection error:", error);
    }
  });
});

function redirectToQuestionPage() {
  window.location.href = "question_page.html";
}
