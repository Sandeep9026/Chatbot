const chatBox = document.getElementById("chat-box");
const chatForm = document.getElementById("chat-form");
const userInput = document.getElementById("user-input");
const clearChatButton = document.getElementById("clear-chat");
const quickActions = document.getElementById("quick-actions");

const avatars = {
    bot: {
        alt: "Mia",
        src: "https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=96&q=80",
    },
    user: {
        alt: "Customer",
        src: "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=96&q=80",
    },
};

const initialBotMessage = `
    <div class="message bot">
        <div class="avatar">
            <img src="${avatars.bot.src}" alt="${avatars.bot.alt}">
        </div>
        <div class="bubble">
            Hi, I'm Mia from Astera support. I can help with order tracking, refund requests, payment issues, address changes, product availability, and connecting you to support.
        </div>
    </div>
`;

function scrollToBottom() {
    chatBox.scrollTop = chatBox.scrollHeight;
}

function createAvatar(role) {
    const avatar = document.createElement("div");
    avatar.className = "avatar";

    const image = document.createElement("img");
    image.src = avatars[role].src;
    image.alt = avatars[role].alt;
    avatar.appendChild(image);

    return avatar;
}

function createMessage(role, text, meta = "") {
    const wrapper = document.createElement("div");
    wrapper.className = `message ${role}`;

    const avatar = createAvatar(role);

    const bubble = document.createElement("div");
    bubble.className = "bubble";
    bubble.textContent = text;

    if (meta) {
        const metaNode = document.createElement("span");
        metaNode.className = "meta";
        metaNode.textContent = meta;
        bubble.appendChild(metaNode);
    }

    wrapper.appendChild(avatar);
    wrapper.appendChild(bubble);
    chatBox.appendChild(wrapper);
    scrollToBottom();
}

function refreshQuickActions(suggestions = []) {
    quickActions.innerHTML = "";
    suggestions.forEach((suggestion) => {
        const button = document.createElement("button");
        button.type = "button";
        button.className = "quick-chip";
        button.textContent = suggestion;
        button.addEventListener("click", () => {
            userInput.value = suggestion;
            userInput.focus();
        });
        quickActions.appendChild(button);
    });
}

function createTypingIndicator() {
    const typingMessage = document.createElement("div");
    typingMessage.className = "message bot typing-row";
    typingMessage.innerHTML = `
        <div class="avatar">
            <img src="${avatars.bot.src}" alt="${avatars.bot.alt}">
        </div>
        <div class="bubble typing-bubble">
            <span></span><span></span><span></span>
        </div>
    `;
    return typingMessage;
}

async function sendMessage(message) {
    createMessage("user", message);
    userInput.value = "";
    userInput.disabled = true;

    const typingMessage = createTypingIndicator();
    chatBox.appendChild(typingMessage);
    scrollToBottom();

    try {
        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ message }),
        });

        const data = await response.json();
        typingMessage.remove();
        const meta = `${data.intent.replaceAll("_", " ")} - confidence ${data.confidence}`;
        createMessage("bot", data.reply, meta);
        refreshQuickActions(data.suggestions || []);
    } catch (error) {
        typingMessage.remove();
        createMessage("bot", "Something went wrong while connecting to the chatbot service.");
    } finally {
        userInput.disabled = false;
        userInput.focus();
    }
}

chatForm.addEventListener("submit", async (event) => {
    event.preventDefault();
    const message = userInput.value.trim();
    if (!message) {
        return;
    }

    await sendMessage(message);
});

clearChatButton.addEventListener("click", () => {
    chatBox.innerHTML = initialBotMessage;
    refreshQuickActions([
        "Track my order",
        "Change delivery address",
        "Payment failed",
        "Refund policy",
    ]);
    userInput.focus();
});

quickActions.querySelectorAll(".quick-chip").forEach((button) => {
    button.addEventListener("click", () => {
        userInput.value = button.textContent;
        userInput.focus();
    });
});
