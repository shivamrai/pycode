class Solution:

    def __init__(self):
        # Define word mappings for numbers below 20
        self.below_20 = [
            "",
            "One",
            "Two",
            "Three",
            "Four",
            "Five",
            "Six",
            "Seven",
            "Eight",
            "Nine",
            "Ten",
            "Eleven",
            "Twelve",
            "Thirteen",
            "Fourteen",
            "Fifteen",
            "Sixteen",
            "Seventeen",
            "Eighteen",
            "Nineteen",
        ]
        # Define word mappings for tens (20, 30, 40, etc.)
        self.tens = [
            "",
            "",
            "Twenty",
            "Thirty",
            "Forty",
            "Fifty",
            "Sixty",
            "Seventy",
            "Eighty",
            "Ninety",
        ]
        # Define scale words for thousands, millions, billions
        self.thousands = ["", "Thousand", "Million", "Billion"]

    def _helper(self, n) -> str:
        # Helper function to convert numbers less than 1000 to words
        if n == 0:
            # Return empty string for zero
            return ""
        if n < 20:
            # Use below_20 array for numbers 1-19
            return self.below_20[n] + " "
        if n < 100:
            # For numbers 20-99, combine tens word with recursive call for ones
            return self.tens[n // 10] + " " + self._helper(n % 10)
        # For numbers 100-999, add "Hundred" and recursively process remainder
        return self.below_20[n // 100] + " Hundred " + self._helper(n % 100)

    def numberToWords(self, number: int) -> str:
        if number == 0:
            return "Zero"

        result = ""
        # Initialize index for thousands scale
        i = 0

        # Process number in chunks of 1000
        while number > 0:
            # Check if current chunk (last 3 digits) is non-zero
            if number % 1000 != 0:
                # Convert current chunk to words and prepend to result
                result = self._helper(number % 1000) + self.thousands[i] + " " + result
            # Move to next chunk by dividing by 1000
            number //= 1000
            # Increment scale index
            i += 1

        # Remove trailing spaces and return
        return result.strip()


if __name__ == "__main__":
    sol = Solution()
    test_cases = [123, 12345, 1234567, 1234567891, 0]
    for num in test_cases:
        print(f"{num} -> {sol.numberToWords(num)}")
