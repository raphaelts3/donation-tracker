import _ from 'lodash';

import { ActionFor, ActionTypes } from '../Action';
import { EventDetails, EventDetailsAction } from './EventDetailsTypes';

type EventDetailsState = EventDetails;

const initialState: EventDetailsState = {
  receiverName: '',
  prizesUrl: '',
  rulesUrl: '',
  donateUrl: '',
  minimumDonation: 1,
  maximumDonation: Infinity,
  step: 0.01,
  availableIncentives: {},
  prizes: [],
};

function handleLoadEventDetails(state: EventDetailsState, action: ActionFor<'LOAD_EVENT_DETAILS'>) {
  const { eventDetails } = action;

  return {
    ...eventDetails,
    availableIncentives: {
      ...eventDetails.availableIncentives,
    },
    prizes: [...eventDetails.prizes],
  };
}

export default function reducer(state = initialState, action: EventDetailsAction) {
  switch (action.type) {
    case ActionTypes.LOAD_EVENT_DETAILS:
      return handleLoadEventDetails(state, action);
    default:
      return state;
  }
}
