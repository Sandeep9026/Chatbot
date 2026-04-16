from __future__ import annotations

from dataclasses import dataclass
from difflib import SequenceMatcher
import re
from typing import Dict, List, Optional


@dataclass(frozen=True)
class Intent:
    name: str
    patterns: List[str]
    response: str
    suggestions: List[str]


class CustomerServiceChatbot:
    def __init__(self) -> None:
        self.intents = self._build_intents()

    def _build_intents(self) -> List[Intent]:
        return [
            Intent(
                name="greeting",
                patterns=[
                    "hello",
                    "hi",
                    "hey",
                    "good morning",
                    "good evening",
                    "is anyone there",
                    "can you help me",
                ],
                response=(
                    "Hello and welcome to Astera support. I can help with order tracking, delivery delays, "
                    "returns, payments, address updates, account issues, promo code problems, and support contact details."
                ),
                suggestions=["Track my order", "Refund policy", "Change delivery address"],
            ),
            Intent(
                name="order_tracking",
                patterns=[
                    "where is my order",
                    "track my order",
                    "track order",
                    "order status",
                    "delivery status",
                    "when will my order arrive",
                    "my order has not arrived",
                ],
                response=(
                    "You can check the latest status from the Orders section using your order ID and registered email. "
                    "If tracking has not updated for more than 48 hours, support can raise a courier check."
                ),
                suggestions=["Delivery is delayed", "Talk to support", "Change delivery address"],
            ),
            Intent(
                name="shipping",
                patterns=[
                    "shipping time",
                    "delivery time",
                    "how long does shipping take",
                    "how many days for delivery",
                    "shipping charges",
                    "express delivery",
                    "international shipping",
                ],
                response=(
                    "Standard delivery usually takes 3 to 5 business days. Express shipping takes 1 to 2 business days in eligible areas. "
                    "Final delivery charges are shown during checkout."
                ),
                suggestions=["Track my order", "Payment methods", "Product availability"],
            ),
            Intent(
                name="delivery_delay",
                patterns=[
                    "delivery is delayed",
                    "my order is delayed",
                    "package is late",
                    "why is my order late",
                    "order delayed",
                    "delivery delay",
                ],
                response=(
                    "Delays can happen because of courier backlog, weather conditions, address verification, or failed delivery attempts. "
                    "If the order has been stuck for more than 48 hours, please contact support with your order reference."
                ),
                suggestions=["Track my order", "Talk to support", "Change delivery address"],
            ),
            Intent(
                name="refund",
                patterns=[
                    "refund policy",
                    "i want a refund",
                    "how do i get a refund",
                    "money back",
                    "refund status",
                    "can i return my order",
                    "return item",
                ],
                response=(
                    "Eligible items can usually be returned within 7 days of delivery if they are unused and in original condition. "
                    "Once a return is approved, refunds are typically completed within 5 to 7 business days."
                ),
                suggestions=["Start a return", "Cancel my order", "Talk to support"],
            ),
            Intent(
                name="return_process",
                patterns=[
                    "start a return",
                    "return process",
                    "how to return item",
                    "schedule return pickup",
                    "pickup for return",
                    "return request",
                ],
                response=(
                    "To start a return, open your order details, select Return Item, choose the reason, and confirm the pickup address. "
                    "You will receive an update as soon as the return request is approved."
                ),
                suggestions=["Refund policy", "Track my order", "Talk to support"],
            ),
            Intent(
                name="cancel_order",
                patterns=[
                    "cancel order",
                    "i want to cancel my order",
                    "order cancellation",
                    "stop my purchase",
                    "cancel before shipping",
                    "can i cancel after placing order",
                ],
                response=(
                    "Orders can usually be cancelled before they move to packing or shipping. "
                    "Open the order details page and choose Cancel Order. If the option is unavailable, the order may already be in process."
                ),
                suggestions=["Refund policy", "Track my order", "Talk to support"],
            ),
            Intent(
                name="payment",
                patterns=[
                    "payment methods",
                    "how can i pay",
                    "can i pay with upi",
                    "credit card accepted",
                    "cash on delivery",
                    "wallet payment",
                ],
                response=(
                    "We support UPI, debit cards, credit cards, net banking, and selected digital wallets. "
                    "Cash on delivery may be available depending on location and order value."
                ),
                suggestions=["Payment failed", "Refund policy", "Promo code issue"],
            ),
            Intent(
                name="payment_failed",
                patterns=[
                    "payment failed",
                    "transaction failed",
                    "money deducted but order not confirmed",
                    "billing failed",
                    "card declined",
                    "payment problem",
                ],
                response=(
                    "If payment failed but money was deducted, please wait up to 30 minutes for an automatic reversal. "
                    "If the amount is not reversed, contact support with the transaction ID for manual review."
                ),
                suggestions=["Talk to support", "Payment methods", "Refund policy"],
            ),
            Intent(
                name="account_help",
                patterns=[
                    "login problem",
                    "forgot password",
                    "reset my password",
                    "cannot sign in",
                    "unable to login",
                    "account locked",
                    "account help",
                ],
                response=(
                    "Use the Forgot Password option on the sign-in page to reset access. "
                    "If your account is locked or still inaccessible, support can verify your identity and help restore it."
                ),
                suggestions=["Talk to support", "Store hours", "Payment methods"],
            ),
            Intent(
                name="address_change",
                patterns=[
                    "change delivery address",
                    "change shipping address",
                    "update address",
                    "wrong address",
                    "modify delivery location",
                    "address change",
                ],
                response=(
                    "You can update the delivery address before the order is shipped. "
                    "Open your order details and choose Edit Address. If the order is already packed, please contact support right away."
                ),
                suggestions=["Track my order", "Cancel my order", "Talk to support"],
            ),
            Intent(
                name="product_availability",
                patterns=[
                    "is this product in stock",
                    "product availability",
                    "when will it be back",
                    "out of stock",
                    "restock date",
                    "available size",
                ],
                response=(
                    "Product availability is updated live on the product page. "
                    "If an item is out of stock, you can use the notify option to get an alert when it returns."
                ),
                suggestions=["Notify me when available", "Shipping time", "Talk to support"],
            ),
            Intent(
                name="promo_code",
                patterns=[
                    "promo code issue",
                    "coupon not working",
                    "discount code invalid",
                    "offer not applying",
                    "promo code",
                    "coupon failed",
                ],
                response=(
                    "Please check whether the coupon has expired, whether the minimum order value is met, and whether the selected items are eligible. "
                    "Some offers are limited to one use per account."
                ),
                suggestions=["Payment methods", "Talk to support", "Shipping time"],
            ),
            Intent(
                name="store_hours",
                patterns=[
                    "store hours",
                    "working hours",
                    "support timings",
                    "when are you open",
                    "business hours",
                    "what time support available",
                ],
                response=(
                    "Our customer support team is available Monday to Saturday from 9:00 AM to 7:00 PM. "
                    "Messages sent after hours are handled in the next working window."
                ),
                suggestions=["Talk to support", "Track my order", "Refund policy"],
            ),
            Intent(
                name="contact_support",
                patterns=[
                    "contact support",
                    "talk to agent",
                    "speak to human",
                    "customer care number",
                    "email support",
                    "help center",
                    "representative",
                ],
                response=(
                    "You can contact the care team at support@asterahelp.com or call +91-90000-12345 during support hours. "
                    "Sharing your order ID and issue summary helps the team resolve the case faster."
                ),
                suggestions=["Store hours", "Track my order", "Payment failed"],
            ),
            Intent(
                name="goodbye",
                patterns=[
                    "bye",
                    "goodbye",
                    "thanks",
                    "thank you",
                    "see you",
                    "ok thanks",
                ],
                response="Happy to help. If you need anything else, just send another message.",
                suggestions=["Track my order", "Refund policy", "Talk to support"],
            ),
        ]

    def _normalize(self, text: str) -> str:
        text = text.lower()
        text = re.sub(r"[^a-z0-9\s]", " ", text)
        return re.sub(r"\s+", " ", text).strip()

    def _keyword_score(self, message: str, pattern: str) -> float:
        message_words = set(message.split())
        pattern_words = set(pattern.split())
        if not pattern_words:
            return 0.0

        overlap = len(message_words & pattern_words)
        return overlap / len(pattern_words)

    def _pattern_score(self, message: str, pattern: str) -> float:
        similarity = SequenceMatcher(None, message, pattern).ratio()
        keyword_score = self._keyword_score(message, pattern)
        contains_bonus = 0.15 if pattern in message else 0.0
        return max(similarity, keyword_score + contains_bonus)

    def _extract_order_id(self, message: str) -> Optional[str]:
        match = re.search(r"\b(?:ord|order)[-\s:]?(\d{4,10})\b", message, re.IGNORECASE)
        if match:
            return f"ORD-{match.group(1)}"
        return None

    def _fallback_response(self, message: str) -> Dict[str, object]:
        order_id = self._extract_order_id(message)
        if order_id:
            reply = (
                f"I noticed the reference {order_id}. I cannot fetch live order data in this build, "
                "but I can still guide you on tracking, cancellation, returns, address changes, and support escalation."
            )
            suggestions = ["Track my order", "Change delivery address", "Talk to support"]
        else:
            reply = (
                "I do not have a precise answer for that yet, but I can help with tracking, delivery delays, returns, "
                "payments, coupon issues, account access, store hours, and support contact details."
            )
            suggestions = ["Track my order", "Payment failed", "Refund policy"]

        return {
            "reply": reply,
            "intent": "fallback",
            "confidence": 0.0,
            "suggestions": suggestions,
        }

    def get_response(self, message: str) -> Dict[str, object]:
        normalized_message = self._normalize(message)
        best_intent = None
        best_score = 0.0

        for intent in self.intents:
            intent_score = max(
                self._pattern_score(normalized_message, self._normalize(pattern))
                for pattern in intent.patterns
            )
            if intent_score > best_score:
                best_score = intent_score
                best_intent = intent

        if best_intent is None or best_score < 0.45:
            return self._fallback_response(message)

        reply = best_intent.response
        order_id = self._extract_order_id(message)
        if order_id and best_intent.name in {"order_tracking", "delivery_delay", "cancel_order"}:
            reply = f"For {order_id}, {reply}"

        return {
            "reply": reply,
            "intent": best_intent.name,
            "confidence": round(best_score, 2),
            "suggestions": best_intent.suggestions,
        }
