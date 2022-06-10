class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        """
        logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
        """
        # Place all the letter logs at the beginning
        def is_letter_log(log):
            return log.split(' ')[1].isalpha()
        
        ordered_logs = []
        for current_log in logs:
            if is_letter_log(current_log):
                ordered_logs.append(current_log)
        
        # Sort the letter logs
        def getLetterLogKey(log):
            log = log.split(' ')
            secondary = log.pop(0)
            primary = ' '.join(log)
            return primary, secondary
        ordered_logs = sorted(ordered_logs, key=getLetterLogKey)
        
        # Append the remaining digit logs
        def is_digit_log(log):
            return log.split(' ')[1].isnumeric()
        
        for current_log in logs:
            if is_digit_log(current_log):
                ordered_logs.append(current_log)
        
        return ordered_logs
        
        
        